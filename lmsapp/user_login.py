from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from . import EmailBackend
from django.contrib.auth import authenticate, login,logout 

def REGISTER(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exists')
            return redirect('register')
        
        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username already exists')
            return redirect('register')
        
        # Create the user
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Error: {e}')
            return redirect('register')
    
    return render(request, 'registration/register.html')

def DOLOGIN(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"Email: {email}, Password: {password}")  # Debugging print
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            print("User authenticated successfully")  # Debugging print
            login(request, user)
            messages.success(request, 'Welcome to home page!')
            return redirect('home')
        else:
            print("Authentication failed")  # Debugging print
            messages.error(request, 'Email and password are Invalid!')
            return redirect('login')
    else:
        return render(request, 'login.html')
  # Render the login page on GET request
    
