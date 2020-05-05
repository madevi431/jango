from django.contrib import admin
from user.models import candidate
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
	list_display=['first_name','last_name','user_name','age','email','password','contact']
admin.site.register(candidate,EmployeeAdmin)