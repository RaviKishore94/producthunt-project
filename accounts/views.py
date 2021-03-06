from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def signup(request):
	if request.method == 'POST':
		if request.POST['inputPassword'] == request.POST['inputPasswordConfirm']:
			try:
				user = User.objects.get(username = request.POST['inputUserName'])
				return render(request, 'accounts/signup.html', {'error': 'Username has already been taken.'})
			except User.DoesNotExist:
				user = User.objects.create_user(username = request.POST['inputUserName'], password = request.POST['inputPassword'])
				return redirect('login')
		else:
			return render(request, 'accounts/signup.html', {'error': 'Passwords do not Match. Please try again.'})
	else:
		return render(request, 'accounts/signup.html')

def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username = request.POST['inputUserName'], password = request.POST['inputPassword'])
		if user is not None:
			auth.login(request, user)
			return redirect('home')
		else:
			return render(request, 'accounts/login.html', {'error': 'Username or Password is incorrect.'})
	else:
		return render(request, 'accounts/login.html')

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return render(request, 'accounts/logout.html')
