from django.shortcuts import render,redirect
from .models import MyFileUpload
from .forms import MyFileForm
from django.contrib import messages
from django.urls import path 
import os

# Create your views here.


def home (request):

    my_data = MyFileUpload.objects.all()

    my_form = MyFileForm()

    if(my_data != " "):

        context = {'forms':my_form,'mydata':my_data}

        return render(request,'index.html',context)
    
    else:

        context = {'forms':my_form}

        return render(request,"index.html",context)

def uploadfile(request):

    if(request.method == "POST"):

        my_form = MyFileForm(request.POST,request.FILES)

        if(my_form.is_valid()):

            MyFileName = request.POST.get("file_name")

            MyFile = request.FILES.get("file")

            exits = MyFileUpload.objects.filter(my_file = MyFile).exists()

            if(exits):

                messages.error(request,"The File %s is Aleardy exists...!!!"% MyFile)

            else:

                MyFileUpload.objects.create(file_name = MyFileName,my_file = MyFile).save()

                messages.success(request,"File Upload Successfully...!!!")

        return redirect("Home")

def deleteFile(request,id):

    my_data = MyFileUpload.objects.get(id = id)

    my_data.delete()

    os.remove(my_data.my_file.path)

    messages.success(request,"File deleted Successfully.")

    return redirect("Home")