from django.shortcuts import get_object_or_404, render,redirect
from .forms import LoginForm
from django.http import HttpResponseRedirect,HttpResponseForbidden
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify
from profiles.models import Employee
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User


# Create your views here.

def user_is_admin(user):
    return user.is_authenticated and user.is_superuser

def login_page(request):
    if request.method=="POST":
        username=request.POST["user_name"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user_is_admin(user):
                return redirect('all')
            employee = get_object_or_404(Employee, username=username)
            slug=employee.slug

            return redirect('detail',slug)
        else:
            return HttpResponseRedirect('login')
    else:
        form=LoginForm()
    return render(request,"login.html",{
        "form":form
    })

def sign(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            employee = get_object_or_404(Employee, username=username)
            slug=employee.slug
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('detail' ,slug)
    else:
        form=UserCreationForm()
    return render(request,'signup.html',{
        "form":form
    })

def logout_user(request):
    logout(request)
    return redirect("login_page")