from django.contrib import admin

# Register your models here.
from account.models import signup
class display(admin.ModelAdmin):
	list_display=['password','email','tempassword']
admin.site.register(signup,display)