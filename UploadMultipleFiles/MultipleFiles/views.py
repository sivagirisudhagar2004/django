from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.urls import path
import os


# Create your views here.

def home(request):

    mydata = MyfileUpload.objects.all()

    myfile = MyFileForm()

    if(myfile != ""):

        context = {'form':myfile,'mydata':mydata}

        return render(request,"index.html",context)
    else:

        context = {"form":myfile}

        return render(request,"index.html",context)

def uploadfile(request):

    if(request.method == "POST"):

        myfile = MyFileForm(request.POST,request.FILES)

        if(myfile != ""):

            for Myfile in request.FILES.getlist('file'):

                exists = MyfileUpload.objects.filter(my_file = Myfile).exists()

                if(exists):

                    data = 1
                else:
                    data = 0

                    MyfileUpload.objects.create(my_file = Myfile).save()

            if(data == 1):

                messages.success(request,"The File already exists...!!!")
            else:

                messages.success(request,"The File Upload Successfully...!!!")

            return redirect("Home")
        
def deletefile(request,id):

    mydata = MyfileUpload.objects.get(id = id)

    mydata.delete()

    os.remove(mydata.my_file.path)

    messages.success(request,"File Deleted Successfully...!!!")

    return redirect("Home")

def deleteall(request):

    if(request.method == "POST"):

        my_id = request.POST.getlist('id[]')

        for id in my_id:

            data = MyfileUpload.objects.get(id = id)

            data.delete()

            os.remove(data.my_file.path)

            messages.success(request,"File Deleted Successfully...!!!")
            
        return redirect("Home")







