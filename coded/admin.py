from django.contrib import admin
from coded.models import Coded
# Register your models here.


@admin.register(Coded)
class CodedAdmin(admin.ModelAdmin):
    list_display = ["id","title","Date"]
