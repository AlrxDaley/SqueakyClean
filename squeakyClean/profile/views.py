from django.shortcuts import  render, redirect
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib import messages

def register_request(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index.html")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = SignUpForm()
	return render (request=request, template_name="signup.html", context={"register_form":form})