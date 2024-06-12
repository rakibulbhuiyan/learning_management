from django.shortcuts import render,redirect

# Create your views here.
def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'main/home.html')

def single_course(request):
    return render(request, 'main/single_course.html')

def about_us(request):
    return render(request, 'main/about_us.html')
    
def contact_us(request):
    return render(request, 'main/contact_us.html')