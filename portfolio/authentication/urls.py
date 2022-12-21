from django.urls import path
from authentication import views

urlpatterns = [
    path('', views.login, name = 'login'),
    path('registration/', views.registration, name = 'registration'),
    path('forgetpassword', views.forgetpassword, name = 'forgetpassword'),
]
