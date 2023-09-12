from django.shortcuts import render, redirect
from . forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


def signup(request): #created a view signup to display the SignUpForm from forms.py
	form = SignUpForm() 
	
	if request.method == 'POST':
		form = SignUpForm(request.POST)
	
	if form.is_valid():
		form.save()
		messages.success(request,'Account Created')
		return redirect('signin')
	
	context = {'form':form}
	'''returning a page with signup file from 
	templates with the SignUpForm'''
	return render(request, 'signup.html',context) 

def signin(request): #login view
	'''if statement to check if the fetch username and password 
	and check if they match the ones in the login'''
	if request.method == 'POST': 
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username,password=password)
		
		'''if statement to check if user is true 
		and redirects to homepage'''
		if user is not None:
			login(request,user)
			return redirect('home')
		else:
			messages.info(request,'wrong username or password')

	context = {} 
	return render(request,'login.html',context)

def homePage(request):
	context = {}
	return render(request,'homepage.html',context)

def logoutPage(request):
	logout(request)
	return redirect('signin')