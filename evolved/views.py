from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .utils import main
from .utils2 import main2

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def home(request):
    return render(request, "home.html")

def cook(request):
    return render(request, "cook.html")


def content_based(request):
    if request.method == "POST":
        address = request.POST.get("address")
        specialty = request.POST.get("specialty")
        # Call your model's main function with cook_id as an argument
        results = main(address, specialty)
        # Render the same page with the results
        return render(request, "content_based.html", {"results": results})

    # Render the home page
    return render(request, "content_based.html")

def collaborative(request):
    if request.method == "POST":
        cook_id = int(request.POST.get("cook_id"))
        # Call your model's main function with cook_id as an argument
        results = main2(cook_id)
        # Render the same page with the results
        return render(request, "collaborative.html", {"results": results})

    # Render the home page
    return render(request, "collaborative.html")