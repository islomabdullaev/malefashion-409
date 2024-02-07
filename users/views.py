from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('pages:home')
        else:
            return redirect('users:signin')

    return render(request, template_name='registration/signin.html')


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        if password == password_confirm:
            user = User.objects.filter(username=username).exists()
            if user:
                return HttpResponse("User already exsists !")
            else:
                user = User.objects.create_user(username=username, password=password)
                login(request, user)
                return redirect('pages:home')
        else:
            return HttpResponse('Password do not match !')
    return render(request, template_name="registration/signup.html")


def signout(request):
    logout(request)
    return redirect('pages:home')