from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

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
    return render(request, template_name="registration/signup.html")


def signout(request):
    logout(request)
    return redirect('pages:home')