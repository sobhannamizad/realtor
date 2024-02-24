from django.db import models
from accounts.models import User
from ads.models import Property

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='cart')
    property = models.ForeignKey(Property,on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return f'{self.user.full_name}-{self.property.title} - {self.is_paid}'