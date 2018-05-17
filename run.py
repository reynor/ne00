from master.models import Company,Staff
from django.contrib.auth.models import User
c = Company.objects.get(pk=1)
u = User.objects.get(pk=1)
s = Staff(userId=u,userName="王冠雄",job="设计工程师",company=c)
s.save()
s1 = u.staff