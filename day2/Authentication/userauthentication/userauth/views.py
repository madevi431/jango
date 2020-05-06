from django.shortcuts import render
#from django.contrib.auth.forms import UserCreationForm
from userauth.forms import UsersignupForm
from django.http import HttpResponse
#from userauth.forms import UsersignupForm
# Create your views here.
def signup(request):
	#form=UserCreationForm(request.POST)
	if request.method=='POST':

		form=UsersignupForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Done')

	form=UsersignupForm()
	return render(request,'userauth/signup.html',{'form':form})
def home(request):
	return render(request,'userauth/home.html',{})