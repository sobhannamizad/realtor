from django.db import models
from accounts.models import Realtor

class Property(models.Model):
    TYPE_CHOICES = (
        ('R', 'rent'),
        ('S', 'Sale'),
    )
    owner = models.ForeignKey(Realtor,on_delete=models.CASCADE,related_name='ADS')
    title = models.CharField(max_length=150)
    description = models.TextField()
    address = models.TextField()
    type = models.CharField(choices=TYPE_CHOICES,max_length=100)
    price = models.PositiveIntegerField()
    prepayment = models.PositiveIntegerField(blank=True,null=True)
    image = models.ImageField(upload_to='ads',blank=True,null=True)
    is_active = models.BooleanField(default=False)
    is_close = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
