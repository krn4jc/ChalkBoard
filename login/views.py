from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login(response):
    if response == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
        else:
            form = UserCreationForm()
    form = UserCreationForm()
    return render(response, "registration/registration.html", {"form":form})