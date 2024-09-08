from django.http import HttpResponse, HttpResponseRedirect,HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from .models import Employee, Search
from .forms import EmployeeForm, SearchForm,DeleteForm,EditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.utils.text import slugify
from members.models import Login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test

def user_is_admin(user):
    return user.is_authenticated and user.is_superuser

@user_passes_test(user_is_admin)
def index(request):
    employee = Employee.objects.all()
    user = request.user
    return render(request, "all.html", {
        "emp": employee,
        "user": user
    })


@user_passes_test(user_is_admin)
def add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("all")
    else:
        form = EmployeeForm()
    return render(request, "index.html", {
        "form": form
    })

@login_required
def detail(request, slug):
    employee = get_object_or_404(Employee, slug=slug)
    value=False
    user=request.user
    x=str(user)
    if x==str(employee.username) or user_is_admin(user):
        return render(request, "detail.html", {
            "employee": employee,
            "value":user_is_admin(user)
        })
    else:
        return redirect('all')

@user_passes_test(user_is_admin)
def search(request):
    employees = Employee.objects.all()
    form = SearchForm(request.GET)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        department = form.cleaned_data.get('designation')
        position = form.cleaned_data.get('position')
        if name:
            employees = employees.filter(name__icontains=name)
        if department:
            employees = employees.filter(designation=department)
        if position:
            employees = employees.filter(position=position)

    return render(request, "search.html", {
        "employees": employees,
        "form": form
    })

@login_required
def edit(request,slug):
    employee = Employee.objects.get(slug=slug)
    if request.method == 'POST':
        form = EditForm(request.POST,request.FILES, instance=employee)
        if form.is_valid():    
            form.save()
            if 'image' in request.FILES:
                employee.image = request.FILES['image']
            return redirect('detail',slug)
    else:
        form = EditForm(instance=employee)
    return render(request, 'edit.html', {
        'form': form,
        'employee': employee
        })

@user_passes_test(user_is_admin)
def delete(request):
    value=False
    employees = Employee.objects.all()
    form = DeleteForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        emp=Employee.objects.get(email=email)
        emp.delete()
        value=True
        return redirect("all")
    return render(request,"delete.html",{
        "form":form,
        "value":value
    })

@user_passes_test(user_is_admin)
def deleteslug(request,slug):
    value=False
    employee = Employee.objects.get(slug=slug)
    if employee:
        employee.delete()
        value=True
        return redirect("all")
    return render(request,"delete.html",{
        "value":value
    })


