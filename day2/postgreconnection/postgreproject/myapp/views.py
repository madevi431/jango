from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import userregisterform
from myapp.models import userregister
# Create your views here.
def upload(request):
	if request.method=="POST":
		form=userregisterform(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponse("image uploaded")
	form=userregisterform()
	return render(request,'myapp/index.html',{'form':form})
def displayimages(request):
	data=userregister.objects.all()
	return render(request,'myapp/displayimages.html',{'data':data})