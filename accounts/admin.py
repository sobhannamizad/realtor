from django.contrib import admin
from .models import Realtor,User,Vote
from django.contrib.auth.models import Group
admin.site.unregister(Group)
admin.site.register(Realtor)
admin.site.register(User)
admin.site.register(Vote)
