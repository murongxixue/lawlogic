from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(test)
class testAdmin(admin.ModelAdmin):
    list_display = ("id","testa","botname")
