from django.contrib import admin

from . models import Groups
from . models import Users
# Register your models here.
admin.site.register(Groups)
admin.site.register(Users)
