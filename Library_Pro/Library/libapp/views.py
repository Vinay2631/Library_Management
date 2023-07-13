from msilib.schema import Error
from multiprocessing import context
from django import forms
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'This email is already registerd! Please register with different Mail')
                form=UserRegisterForm()
                return render(request, 'register.html', {'form': form})
            else:
                form.save()
                messages.success(request, f'Your account is created! You can login now!')
                return redirect('login')

    else:
        form=UserRegisterForm()
    return render(request, 'register.html', {'form': form})
c=0
def hello(request):
    global c
    if request.user.is_superuser and c==0:
        c+=1
        global book
        book = {'Book1': {'author': 'Vijay', 'available': 10},
    'Book2': {'author': 'Vinay', 'available': 20},
    'Book3': {'author': 'Vikram', 'available': 30}}
    return render(request,"bookhome.html")

def cart(request):
    if request.method == 'POST':
        global book
        selected_option = request.POST.get('selected_option')
        bs=book.get(selected_option)
        if bs.get('available')>0:
            bs['available']-=1
        return render(request,"cart.html")
        
    else:
        return render(request,"cart.html")


def booklist(request):
    books=book
    return render(request, 'booklist.html', {'data': books})
    
def returnbook(request):
    if request.method == 'POST':
        global book
        selected_option = request.POST.get('selected_option')
        bs=book.get(selected_option)
        bs['available']+=1
        return render(request,"returnbook.html")
        
    else:
        return render(request,"returnbook.html")
