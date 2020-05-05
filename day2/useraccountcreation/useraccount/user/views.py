from django.shortcuts import render
from django.http import HttpResponse
from user.forms import candidateform
from user.models import candidate
# Create your views here.
def register(request):
	if request.method=='POST':
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		user_name=request.POST['user_name']
		email=request.POST['email']
		contact=request.POST['contact']
		age=request.POST['age']
		password=last_name+"@123"
		obj=candidate(first_name=first_name,last_name=last_name,user_name=user_name,password=password,email=email,contact=contact,age=age)
		obj.save()
		return HttpResponse("Please use this password"+" "+password+" "+"to login")
# form=candidateform(request.POST)# if form.is_valid():# 	obj=form.cleaned_data
# 	first_name=obj['first_name']
		# 	last_name=obj['last_name']
		# 	user_name=obj['user_name']
		# 	email=obj["email"]
		# 	contact=obj["contact"]
		# 	age=obj["age"]
		# 	password=last_name+"@123"
		# 	form.save()
		
	form=candidateform()
	return render(request,'user/register.html',{'form':form})
	#return render(request,'user/details.html',{'form':form})
def login(request):
	if request.method=="POST":
		user_name=request.POST["username"]
		password=request.POST["password"]
		data=candidate.objects.all().filter(user_name=user_name,password=password)
		print(list(data))
		if data:
			return render(request,'user/profile.html',{'data':data})
		else:
			return HttpResponse("invalid Username or password")
	return render(request,'user/login.html',{})
