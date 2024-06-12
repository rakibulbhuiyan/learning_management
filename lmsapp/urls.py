from django.urls import path,include
from lmsapp import views , user_login

urlpatterns = [
    
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
    path('single_course/', views.single_course, name='single_course'),  
    path('contact_us/', views.contact_us, name='contact_us'),  
    path('about_us/', views.about_us, name='about_us'),  

    path('accounts/register/', user_login.REGISTER, name='register'),
    path('login/', user_login.DOLOGIN, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),

]