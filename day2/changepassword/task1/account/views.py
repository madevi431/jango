from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from account.models import signup

from django.contrib import messages
from django.core.mail import send_mail
from task1 import settings

def login(request):
	if request.method=="POST":
		email=request.POST["email"]
		password=request.POST["password"]
		password1=User.objects.make_random_password(length=6)
		try:
			obj=signup.objects.get(email=email)

			#if signup.objects.get(email=email) and signup.objects.get(tempassword=password):
			if obj.tempassword==password:
				return render(request,'account/reset.html')
			elif obj.password==password:
				return render(request,'account/welcome.html')
			else:
				messages.warning(request,"password is incorrect")

		# xceept:
		# 	try:
		# 		if signup.objects.get(email=email) and signup.objects.get(password=password):
		# 			return render(request,'account/welcome.html')
		# 	except:
		# 		messages.warning(request,"password is incorrect")
			
		except:
			sub="login info"
			body="Use the below credentilas to login\n\nUsername {0}\n\nPassword {1}\n\nlink to portal:http://localhost:8000/login/".format(email,password1)
			receiver=email
			sender=settings.EMAIL_HOST_USER
			send_mail(sub,body,sender,[receiver])
			obj=signup(email=email,tempassword=password1)
			obj.save()
			messages.success(request,'You have sucessfully registered in portal.please check your {} for username and password'.format(email))

			
		
	
	return render(request,'account/login.html')
def reset(request):
	if request.method=="POST":
		oldpassword=request.POST["oldpassword"]
		newpassword=request.POST["newpassword"]
		confirmpassword=request.POST["confirmpassword"]
		try:
			obj=signup.objects.get(tempassword=oldpassword)

			if newpassword==confirmpassword:
				obj.password=newpassword
				obj.save()
				return render(request,'account/welcome.html')
			else:
				messages.warning(request,"newpassword and confirmpassword should be same")
				
		except:
			messages.warning(request,"old password is incorrect")
	return render(request,'account/reset.html')
				



