from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager
from django.core.validators import MinValueValidator,MaxValueValidator
from django.db.models import Avg

class User(AbstractBaseUser):
    # define fields - is_realtor means real state agent
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=200,unique=True)
    code = models.CharField(max_length=10,blank=True,null=True,unique=True)
    balance = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=False)
    is_realtor =models.BooleanField(default=False)
    is_admin =models.BooleanField(default=False)

    objects= UserManager()

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ('full_name','code',)

    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_lable):
        return True
    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return f"id: {self.id} - {self.full_name} - {self.balance} - {self.is_realtor}"

class Realtor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    address =models.TextField()
    description =models.TextField(blank=True,null=True)
    rate = models.PositiveIntegerField()
    stars_average = models.IntegerField(null=True,blank=True,validators=[MaxValueValidator(5),MinValueValidator(0)])
    is_block = models.BooleanField(default=False)

    def __str__(self):
        return f"id: {self.id} - {self.user.email} -{self.is_active}"

    def calculate_average_stars(self):
        stars = self.stars.all()
        return stars.aggregate(Avg("vote",))['vote__avg']

class OTP(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user} - {self.code}'

class Vote(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    vote =models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(0)])
    realtor = models.ForeignKey(Realtor,on_delete=models.CASCADE,related_name='stars')