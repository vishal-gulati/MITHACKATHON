from django.urls import path,include
from django.contrib.auth import views as authentication_views

urlpatterns = [
    path('login/', authentication_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',authentication_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
