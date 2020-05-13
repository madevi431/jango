from django.shortcuts import render,redirect
from django.http import HttpResponse
from imageupload.forms import uploadform
from imageupload.models import upload

def home(request):
	if request.method=="POST":
		form=uploadform(request.POST,request.FILES)
		if form.is_valid():
			form.save()

		data=upload.objects.all()
			
		return render(request,'imageupload/allimages.html',{'data':data})
	form=uploadform()
	return render(request,'imageupload/home.html',{'form':form})
#def allimages(request):
	#data=upload.objects.all()
	#return render(request,'imageupload/allimages.html',{'data':data})