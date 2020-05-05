from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from mayapp2.forms import StudentForm
from mayapp2.models import Student
# Create your views here.
def hello(request):
	return HttpResponse("haiii")
def register(request):
	if request.method=='POST':
		form=StudentForm(request.POST)
		if form.is_valid():

			form.save()
			messages.success(request,request.POST['stuname']+'record stores successfully')
					#return HttpResponse('Done')
			#return redirect('/mayapp2/reports')
			return redirect('/mayapp2/register')
	form=StudentForm() #with emty paramertes to generate only html form
	return render(request,'mayapp2/register.html',{'form':form})
def reports(request):
	data=Student.objects.all()
	return render(request,'mayapp2/reports.html',{'data':data})


def edit(request,id):
	data=Student.objects.get(id=id)
	if request.method=='POST':
		form=StudentForm(request.POST,instance=data)
		if form.is_valid():
			form.save()
			return redirect("/mayapp2/reports")
	form=StudentForm(instance=data)
	return render(request,'mayapp2/edit.html',{'form':form,'data':data})
def delete(request,id):
	ob=Student.objects.get(id=id)
	if request.method=='POST':
		ob.delete()
		return redirect('/mayapp2/reports')
	return render(request,'mayapp2/msg.html',{'info':ob})