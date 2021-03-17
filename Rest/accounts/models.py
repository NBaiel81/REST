from datetime import date

from django.contrib.auth.models import User
from django.db import models
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    image = models.ImageField()
    full_name = models.CharField(max_length=60)
    birth_date = models.DateField(auto_now_add=True)
    date_join = models.DateTimeField(auto_now_add=True)
    wallet = models.PositiveIntegerField()
    address = models.CharField(max_length=20)



