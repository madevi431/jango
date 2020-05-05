from django.shortcuts import render
from myapp.models import Emp
from django.http import HttpResponse
# Create your views here.
def signup(request):
	if request.method=='POST':
		#here we will read data which is coming from user
		empid=request.POST['empid']
		empName=request.POST['empName']
		empDesig=request.POST['empDesig']
		salary=request.POST['salary']

		obj=Emp(empid=empid,empDesig=empDesig,empName=empName,salary=salary)
		obj.save()
		#return HttpResponse('successfull')
		return redirect('/reports')

	return render(request,'myapp/signup.html')
def reports(request):
	data=Emp.objects.all()
	return render(request,'myapp/reports.html',{'data':data})
