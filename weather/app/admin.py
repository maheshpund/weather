from django.contrib import admin

# Register your models here.
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['id','email','password']


admin.site.register(User,UserAdmin)