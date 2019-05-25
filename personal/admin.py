from django.contrib import admin
from personal.models import User
# Register your models here.


class Useradmin(admin.ModelAdmin):
    list_display = ['username', ]


admin.site.register(User, Useradmin)
