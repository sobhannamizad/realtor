from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager
from django.core.validators import MinValueValidator,MaxValueValidator

class User(AbstractBaseUser):
    # define fields - is_realtor means real state agent
    phone_number = models.CharField(max_length=11,unique=True)
    full_name = models.CharField(max_length=200,unique=True)
    code = models.CharField(max_length=10,blank=True,null=True,unique=True)
    is_active = models.BooleanField(default=True)
    is_realtor =models.BooleanField(default=False)
    is_admin =models.BooleanField(default=False)

    objects= UserManager()

    USERNAME_FIELD ='phone_number'
    REQUIRED_FIELDS = ('full_name','code',)

    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_lable):
        return True
    @property
    def is_staff(self):
        return self.is_admin

class Realtor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    address =models.TextField()
    description =models.TextField(blank=True,null=True)
    rate = models.PositiveIntegerField()
    stars_average = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(0)])
    is_block = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.phone_number} -{self.is_active}"


class Vote(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    vote =models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(0)])
    realtor = models.ForeignKey(Realtor,on_delete=models.CASCADE,related_name='stars')