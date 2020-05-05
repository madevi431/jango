from django.contrib import admin
from mayapp2.models import Student
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
	list_display=['stuid','stuname','branch','age']
admin.site.register(Student,EmployeeAdmin)

