from django.contrib import admin
from myapp.models import Emp
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
	list_display=['empid','empName','empDesig','salary']
admin.site.register(Emp,EmployeeAdmin)
