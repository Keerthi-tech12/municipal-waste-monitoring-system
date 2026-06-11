from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile


def login_view(request):

    error = ""

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            profile = UserProfile.objects.filter(user=user).first()

            if not profile:
               error = "User profile not found"
               return render(request, 'login.html', {'error': error})

            if profile.role == 'Commissioner':
                return redirect('/')

            elif profile.role == 'Zone Officer':
                return redirect('/')

            elif profile.role == 'Data Entry Operator':
                return redirect('/waste-collection/')

        else:

            error = "Invalid Username or Password"

    return render(
        request,
        'login.html',
        {
            'error': error
        }
    )


def logout_view(request):

    logout(request)

    return redirect('/login/')