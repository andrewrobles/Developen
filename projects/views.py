from django.shortcuts import render

from .forms import SignInForm, CreateAccountForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from django.contrib.auth.models import User

def index(request):
	if request.user.is_authenticated:
	    return render(request, 'projects/index.html')
	else:
		return redirect('/projects/sign-in/')

def sign_in(request):
	if request.method == 'POST':
		form = SignInForm(request.POST)

		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)

				return redirect('/projects/')

			else:
				form = SignInForm()
				return render(request, 'projects/sign-in.html', {'form': form})
	else:
		form = SignInForm()
    
	return render(request, 'projects/sign-in.html', {'form': form})

def sign_out(request):
	logout(request)

	return redirect('/projects/sign-in/')

def create_account(request):
	if request.method == 'POST':
		form = CreateAccountForm(request.POST)

		if form.is_valid():
			firstname = form.cleaned_data['firstname']
			lastname = form.cleaned_data['lastname']
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = User.objects.create_user(username=username, email=None, password=password)

			user.firstname = firstname
			user.lastname = lastname

			user.save()

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)

				return redirect('/projects/')

			else:
				form = SignInForm()
				return render(request, 'projects/sign-in.html', {'form': form})

	else:
		form = CreateAccountForm()

	return render(request, 'projects/create-account.html', {'form': form})

def delete_account(request):
	user = request.user

	user.delete()

	return redirect('/projects/sign-in/')
	

