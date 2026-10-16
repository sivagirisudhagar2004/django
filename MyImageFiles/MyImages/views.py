from django.shortcuts import render,redirect
from .forms import *
from .models import Image
from django.contrib import messages
from django.urls import path
import os

# Create your views here.

def home(request):

    mydata = Image.objects.all()

    myform = MyImageForm()

    context = {'form':myform,'data':mydata}

    return render(request,"index.html",context)

def uploadImage(request):

    if(request.method == "POST"):

        myform = MyImageForm(request.POST,request.FILES)

        if(myform.is_valid()):

            for Myfile in request.FILES.getlist('file'):

                exists = Image.objects.filter(image = Myfile).exists()

                if(exists):

                    data = 1

                else:

                    data = 0

                    Image.objects.create(image = Myfile).save()

                if(exists == 1):

                    messages.success(request,"The Image Already Exists...!!!")

                else:

                    messages.success(request,"Image Uploaded Successfully.")

                return redirect("Home")

def deletefile(request,id):

    mydata = Image.objects.get(id = id)

    mydata.delete()

    os.remove(mydata.image.path)

    messages.success(request,"File Deleted Successfully.")

    return redirect("Home")
