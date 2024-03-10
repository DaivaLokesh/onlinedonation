from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from adminmodule.models import Donar,Admin,User


def demofunction(request):
    return HttpResponse("<font color='green'>Online donation management system</font>")

def homefunction(request):
    return render(request,"index.html")

def aboutfunction(request):
    return render(request,"about.html")

def loginfunction(request):
    return render(request,"login.html")

def contactfunction(request):
    return render(request,"contact.html")


def userlogin(request):
    return render(request,"userlogin.html")


def donarlogin(request):
    return render(request,"donarlogin.html")

# def signup(request):
#     return render(request,"signup.html")

def checkadminlogin(request):

    if request.method=="POST":
        adminuname= request.POST["uname"]
        adminpwd=request.POST["pwd"]

    flag=Admin.objects.filter(Q(username=adminuname)&Q(password=adminpwd))
    print(flag)

    if flag:
        return render(request,"adminhome.html")
        #return HttpResponse("login success")

    else:

        return HttpResponse("Login Failed ")




def checkdonarlogin(request):
    if request.method == "POST":
        donaremail = request.POST["email"]
        donarpwd = request.POST["pwd"]

        flag = Donar.objects.filter(Q(email=donaremail) & Q(password=donarpwd))
        print(flag)

        if flag:
            print("Login Success")
            donaremail=request.session["aunmae"]
            return render(request, "donarhome.html", {"donaremail": donaremail})
            # return HttpResponse("login success")

        else:
            msg = "Login Failed"

            return render(request, "donarlogin.html", {"message": msg})


def checkuserlogin(request):
    if request.method == "POST":
        adminuname = request.POST["uname"]
        adminpwd = request.POST["pwd"]

    flag = User.objects.filter(Q(username=adminuname) & Q(password=adminpwd))
    print(flag)

    if flag:
        return render(request, "userhome.html")
        # return HttpResponse("login success")

    else:

        return HttpResponse("Login Failed ")



