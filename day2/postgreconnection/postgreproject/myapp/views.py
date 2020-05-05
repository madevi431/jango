from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import userregisterform
from myapp.models import userregister
from django.core.mail import send_mail
from postgreproject import settings
# Create your views here.
def upload(request):
	if request.method=="POST":
		form=userregisterform(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			sub="haii"
			body='Ia coming from django app'
			receiver=request.POST['email']
			sender=settings.EMAIL_HOST_USER
			send_mail(sub,body,sender,[receiver])
			return HttpResponse("image uploaded")
	form=userregisterform()
	return render(request,'myapp/index.html',{'form':form})
def displayimages(request):
	data=userregister.objects.all()
	return render(request,'myapp/displayimages.html',{'data':data})
def table(request):
	data=userregister.objects.all()
	return render(request,'myapp/table.html',{'data':data})