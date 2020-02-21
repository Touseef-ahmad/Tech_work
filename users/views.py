from django.shortcuts import render, redirect , HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout

def register(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    if request.method == "POST":
        username = request.POST['user_name']
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        password = request.POST['password']

        if User.objects.filter(username=username).count() == 0:
            user = User.objects.create_user(username=username, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            messages.info(request , 'username taken')
            return render(request, 'signup.html')

def login_view(request):
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid username or password')
            return render(request, 'login.html')
    

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')