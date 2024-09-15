from django.contrib import admin
from .models import Mymodel

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Mymodel, MyModelAdmin)

