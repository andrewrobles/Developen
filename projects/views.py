from django.shortcuts import render

from .forms import SignInForm, CreateAccountForm, CreateProjectForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import Http404

from projects.models import Project
from django.contrib.auth.models import User

def index(request):
	user = request.user

	if user.is_authenticated:
		project_list = Project.objects.filter(user=user)
		context = {
			'project_list': project_list
		}
		return render(request, 'projects/index.html', context)
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

def create_project(request):
	if request.method == 'POST':
		form = CreateProjectForm(request.POST)

		if form.is_valid():
			name = form.cleaned_data['name']
			user = request.user

			p = Project(name=name, user=user)

			p.save()

			return redirect('/projects/')
	else:
		form = CreateProjectForm()

	return render(request, 'projects/create-project.html', {'form': form})	
	
def delete_project(request, project_id):
	try:
		project = Project.objects.get(pk=project_id)
	except Project.DoesNotExist:
		raise Http404("Project does not exist")
	
	project.delete()
	
	return redirect('/projects/')

def project_detail(request, project_id):
	try:
		project = Project.objects.get(pk=project_id)
	except Project.DoesNotExist:
		raise Http404("Project does not exist")

	context = {
		'project': project
	}

	return render(request, 'projects/project-detail.html', context)

def home(request):
	return render(request, 'projects/home.html')

	


