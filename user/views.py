from django.shortcuts import render, redirect
from .forms import LoginForm

from django.contrib.auth import login as django_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model,authenticate
from django.contrib import messages
import pdb
def login(request):
	context = {}
	if request.method == 'GET':
		form = LoginForm()
		context['form'] = form
		return render(request, 'users/login.html', context)
	else:
		form = LoginForm(request.POST)
		if form.is_valid():
			password = form.cleaned_data['password']
			user = authenticate(request, username=form.cleaned_data['username'],password=password)
			if user:
				django_login(request, user)
				print('user logged in')

				return redirect('main_website:home')
			else:
				form = LoginForm()
				context['form'] = form
				messages.error(request, 'Password or username incorrect.')
				return render(request, 'users/login.html', context)
		else:
			context['form'] = form


			return render(request, 'users/login.html', context)

def logout(request):
	auth_logout(request)
	return redirect('main_website:home')