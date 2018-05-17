from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Tag(models.Model):
    tag = models.CharField(max_length=20)

# 公司


class Company(models.Model):
    companyName = models.CharField(max_length=200)

# 员工


class Staff(models.Model):
    userId = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    userName = models.CharField(max_length=10)
    department = models.CharField(max_length=20, null=True)
    job = models.CharField(max_length=20, null=True)
    company = models.ForeignKey(
        Company, null=True, on_delete=models.SET_NULL)  # 员工所属公司

# 员工联系方式


class StaffContact(models.Model):
    staffId = models.ForeignKey(Staff, on_delete=models.CASCADE)
    staffPhone = models.CharField(max_length=20, null=True)
    staffPhoneType = models.CharField(max_length=20, null=True)

# 公司联系方式


class CompanyContact(models.Model):
    companyId = models.ForeignKey(Company, on_delete=models.CASCADE)
    companyPhone = models.CharField(max_length=20, null=True)
    companyAddress = models.CharField(max_length=200, null=True)
    CompanyContactType = models.CharField(max_length=20, null=True)


class partUnit(models.Model):
    dimension = models.CharField(max_length=20, unique=True,db_index=True)
    conversion = models.FloatField()
    # def __init__(self, dimension, conversion):


# 产品
s = []  # 一个stack，记录遍历过的有bom表的产品


class Product(models.Model):
    # from master.models import Product  #调试时导入
    productId = models.CharField(max_length=20, unique=True)
    productName = models.CharField(max_length=20, null=True)
    specification = models.TextField(null = True)
    productBrand = models.CharField(max_length=20, null=True)
    # Product.objects.filter(bom__isnull=False)   #返回有BOM的产品
    # 取消反向相对关系  symmetrical=False, 只能在'self'时使用
    #bom = models.ManyToManyField('self', symmetrical=False)
    tags = models.ManyToManyField(Tag)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.productName

    def isRecursion(self):  # 防止引用自身发生递归
        global s
        if self.getBom.all().count():  # 此产品有BOM表
            if s.count(self):  # 判断BOM表中是否为重复项
                print(self, "为重复项", s)
                q = s
                q.append(self)
                s.clear()
                return(q)
            else:
                b = self.getBom.all()  # 获取产品BOM表
                s.append(self)  # 入栈
                print(self, "入栈", s)
                if s:  # 出现循环后s已被清空，无需执行下面操作
                    for a in b:
                        a.isRecursion()
                    if s:  # 防止s被清空后pop()报错
                        s.pop()  # 遍历结束一张BMO，出栈
                        print("上一节点出栈", s)
                        if len(s) == 0:
                            print("无重复项，最后节点：", self)
                            return(s)
        # return(self.bom.filter(bom__isnull=True))

    def getBomItem(self):
        # 自建SQL，通过productId引索bom关系表，返回self的对应BomItem
        print(self.getBom.all())
    def addBomItem(self):
        # 在模型中添加bom项
        pass

    def migrateBom(self):
        # 将模型中的bom写入数据库
        pass

    def getFullParts(self):
        # 返回无子BOM的零件表
        if self.bom.count():
            #print("There is BOM")
            b = self.bom.all()
            for a in b:
                a.isRecursion()
        else:
            # 未读写数据库，应该不会造成过大开销
            bomList.add(self.getBomItem)
            # print(self)


class BomItem(models.Model):
    # 主表反向查询 product.getBom.all()
    parentProductId = models.ForeignKey(Product, related_name = 'getBom', on_delete=models.CASCADE)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE,null = True)
    unitId = models.ForeignKey(partUnit, null=True, on_delete=models.SET_NULL)
    itemCount = models.FloatField()
    note = models.TextField(null = True)
    modified = models.DateField(auto_now=True)

'''
from master.models import Product
a=Product.objects.filter(bom__isnull=False)
b=Product.objects.create(name="Joe"***)
a.bom.add()
Product.objects.filter(product__bom__isnull=True)
a[1].bom.all()  #KE
a[1].bom.filter(bom__isnull=True)
'''
'''
https://docs.djangoproject.com/en/2.0/topics/db/queries/
e = Entry.objects.get(id=3)
e.authors.all() # Returns all Author objects for this Entry.
e.authors.count()
e.authors.filter(name__contains='John')

a = Author.objects.get(id=5)
a.entry_set.all() # Returns all Entry objects for this Author.
'''
