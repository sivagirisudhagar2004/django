from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.

def home(request):

    myform = RegisterForms()

    return render(request,"index.html",{'forms':myform})