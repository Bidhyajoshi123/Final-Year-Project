from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('aboutus', views.aboutPage, name='aboutus'),
    path('room', views.roomPage, name='room'),
    path('contactus', views.contactPage, name='contactus'),
    path('room/<id>',views.rating, name='rating'),
    path('recommend', views.recommend, name='recommend'),



]