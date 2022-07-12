from django.shortcuts import  render, redirect
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib import messages
from products.models import Category
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm #add this
 
def register_request(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("register-success")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
            messages.error(request, form.errors)
    else:
        form = SignUpForm() 
        
    categories = Category.objects.all 
    return render (request=request, template_name="signup.html", context={"register_form":form,'categories':categories})

def register_success(request):
    
    return render(request, 'register_success.html')

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	else:
		form = AuthenticationForm()
  
	categories = Category.objects.all 
  
	return render(request=request, template_name="login.html", context={"login_form":form,'categories':categories})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")