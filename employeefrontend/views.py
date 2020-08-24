from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
#from .forms import SignUpForm, EditProfileForm

#LOGIN
def login_home(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None: #This means If the user exists
			login(request, user)
			messages.success(request, ('You Are Logged in'))
			return redirect('main')
		else:
			messages.success(request, ('Error Logging In - Please Try Again...'))
			return redirect('login')
	else:
		return render(request, "authenticate/login.html", {})

#LOGOUT
def logout_user(request):
	logout(request)
	messages.success(request, ('You Have been Logged out'))
	return redirect('login')

#MAIN
def main(request):
	return render(request, "authenticate/main.html", {})
