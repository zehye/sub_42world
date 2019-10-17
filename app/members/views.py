from django.contrib.auth import authenticate
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            next = request.GET['next']
            if next:
                return redirect('index')
        else:
            return redirect('members:login')
    else:
        return render(request, 'members/login.html')


def logout(request):
    logout(request)
    return redirect('index')


