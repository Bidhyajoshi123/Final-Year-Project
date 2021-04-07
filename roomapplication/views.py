from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

import json

from django.contrib.auth.decorators import login_required

from .models import Room, Rating


# Create your views here.

def home(request):
    return render(request, 'home.html')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserRegisterForm()
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully..')
                return redirect('login')
        context = {
            'user_form': UserRegisterForm
        }

    return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "username or password is incorrect...")
        context = {}
        return render(request, "login.html", context)


def logoutUser(request):
    logout(request)
    return render(request, "home.html")


def aboutPage(request):
    return render(request, 'aboutus.html')

@login_required(login_url="login")
def roomPage(request):
    data = {
        'roomsData': Room.objects.all()
    }
    return render(request, 'room.html', data)


def contactPage(request):
    return render(request, 'contactus.html')


def rating(request, id):
    if not request.user.is_authenticated:
        return redirect("login")
    if not request.user.is_active:
        raise Http404
    location = get_object_or_404(Room, id=id)

    if request.method == "POST":
        rate = request.POST['rating']
        ratingObject = Rating()
        ratingObject.user = request.user
        ratingObject.location = location
        ratingObject.rating = rate
        ratingObject.save()

        return redirect("room")

    ID = Room.objects.get(id=id)
    data = {
        'roomsData': ID
    }
    return render(request, 'rating.html', data)
