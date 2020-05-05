from django.contrib import admin
from .models import Emp
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
	list_display=['first_name','last_name']
admin.site.register(Emp,EmployeeAdmin)