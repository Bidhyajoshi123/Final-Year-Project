from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

import json
from ast import literal_eval as make_tuple

from django.contrib.auth.decorators import login_required

from .models import *
import requests

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
    # room = Room.objects.all()
    # paginator = Paginator(room, 6)
    # page = request.GET.get('page')
    # try:
    #     rooms = paginator.page(page)
    # except PageNotAnInteger:
    #     rooms = paginator.page(1)
    # except EmptyPage:
    #     rooms = paginator.page(paginator.num_pages)
    # data = {
    #     'roomsData': rooms,
    #     'page': page
    # }

    # page = request.GET.get('page')
    # try:
    #     post_list = paginator.page(page)
    # except PageNotAnInteger:
    #
    #     post_list = paginator.page(1)
    # except EmptyPage:
    #
    #     post_list = paginator.page(paginator.num_pages)
    # return render(request, 'room.html',{'roomsData':post_list,'page':page})

    room = Room.objects.all()
    paginator = Paginator(room, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'room.html', {'page_obj': page_obj})


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




@login_required(login_url='login')
def recommend(request):
    user_id = request.user.id
    url = "http://127.0.0.1:5000/recommend"
    payload = {'user_id':user_id}
    headers = {
        'content-type': "multipart/form-data",
        'cache-control': "no-cache",

    }

    responses = requests.request("POST",url,data=payload)
    # import pdb;pdb.set_trace()
    response = json.loads(responses.text)
    respnses_tuple = make_tuple(response)
    context = list()

    for user_id in respnses_tuple:
        try:
            recommended = Room.objects.get(id=user_id)
            context.append(recommended)
        except:
            pass

    return render(request,"recommend.html",{'context': context})
