from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
import copy
import json

# Create your models here.
#日期转json
# class CJSONEncoder(self,o):
#     if isinstance(o,datetime.datetime):
#         return o.strftime("%Y-%m-%d %H-%M-%S")
#     if isinstance(o,datetime.date):
#         return o.strftime("%Y-%m-%d")


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
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)  # 员工所属公司

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
    dimension = models.CharField(max_length=20, unique=True, db_index=True)
    conversion = models.FloatField()
    # def __init__(self, dimension, conversion):


# 产品
s = []  # 一个stack，记录遍历过的有bom表的产品
resultList = []  # 因递归经常产生 None 返回，使用此变量储存结果


class Product(models.Model):
    # from master.models import Product  #调试时导入
    productId = models.CharField(max_length=20, unique=True, db_index=True)
    productName = models.CharField(max_length=20, null=True, db_index=True)
    #specification = models.TextField(null=True, db_index=True)
    specification = models.CharField(max_length=200,null=True, db_index=True)
    productBrand = models.CharField(max_length=20, null=True, db_index=True)
    # Product.objects.filter(bom__isnull=False)   #返回有BOM的产品
    # 取消反向相对关系  symmetrical=False, 只能在'self'时使用
    #bom = models.ManyToManyField('self', symmetrical=False)
    note = models.TextField(null=True)
    tags = models.ManyToManyField(Tag)
    modified = models.DateTimeField(auto_now=True)
    modiUser = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.productName

    def toJSON(self):  
        fields = []  
        for field in self._meta.fields:  
            fields.append(field.name)  
        
        d = {}
        for attr in fields:  
            if isinstance(getattr(self, attr),datetime.datetime):  
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d %H:%M:%S')  
            elif isinstance(getattr(self, attr),datetime.date):  
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d')  
            else:  
                d[attr] = getattr(self, attr)  
        
        return json.dumps(d)  

    def isRecursion(self):  # 防止引用自身发生递归  #实际为私有方法
        global s, resultList
        if self.Bom.all().count():  # 此产品有BOM表
            if s.count(self):  # 判断BOM表中是否为重复项
                print(self, "为重复项", s)
                s.append(self)
                resultList = copy.copy(s)
                s.clear()
                return(resultList)
            else:
                b = self.Bom.all()  # 获取产品BOM表
                #print(b)
                s.append(self)  # 入栈
                #print(self, "入栈", s)
                if s:  # 出现循环后s已被清空，无需执行下面操作
                    for a in b:
                        a.product.isRecursion()
                    if s:  # 防止s被清空后pop()报错
                        s.pop()  # 遍历结束一张BMO，出栈
                        #print("上一节点出栈", s)
                        if len(s) == 0:
                            print("无重复项，最后节点：", self)
                            resultList = copy.copy(s)
                            return(s)
        # return(self.bom.filter(bom__isnull=True))

    def isErrorBom(self):
        global resultList
        resultList.clear()
        self.isRecursion()
        return resultList

    def getFullParts(self):  # 配合BomItem中的同名方法使用
        # 返回无子BOM的零件表
        global resultList
        resultList.clear()
        b = self.Bom.all()
        n = 0
        for a in b:
            n = n+1
            print("第%d次循环" % n)
            #bomList.append(a)
            print(a.getFullParts())
            #bomList.append(a.getFullParts())
        return(resultList)


class BomItem(models.Model):
    # 主表反向查询 product.Bom.all()
    parentProduct = models.ForeignKey(Product, related_name='Bom', null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    unit = models.ForeignKey(partUnit, null=True, on_delete=models.SET_NULL)
    itemCount = models.FloatField()
    note = models.TextField(null=True)
    modified = models.DateTimeField(auto_now=True)
    modiUser = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.product.productName + ":" + str(self.itemCount)

    def getFullParts(self):  # 实为内部函数，配合Product中同名方法使用
        # 返回无子BOM的零件表
        if self.product.Bom.all().count():
            print("There is BOM:    "+self.__str__())
            b = self.product.Bom.all()
            for a in b:
                a.itemCount = a.itemCount * self.itemCount
                a.getFullParts()
        else:
            print("写入列表:    "+self.__str__())
            resultList.append(self)


'''
from master.models import Product,BomItem,Staff
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
