from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Person)
class ProAdmin(admin.ModelAdmin):
    list_display=('user','build','room','seat','date','starttime','endtime','is_book')
admin.site.register(Seat,ProAdmin)