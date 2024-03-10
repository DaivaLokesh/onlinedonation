from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from adminmodule.models import User,usercontact


# Create your views here.
def viewdonations(request):

    return render(request,"viewdonations.html")

def userhome(request):
    useremail = request.session["auname"]
    return render(request,"userhome.html",{"useremail":useremail})


def checkuserlogin(request):
    if request.method == "POST":
        useremail = request.POST["email"]
        userpwd = request.POST["pwd"]

        flag = User.objects.filter(Q(email=useremail) & Q(password=userpwd))
        print(flag)

        if flag:
            print("Login Success")
            request.session["auname"] = useremail
            return render(request, "userhome.html", {"useremail": useremail})
            # return HttpResponse("login success")

        else:
            msg = "Login Failed"

            return render(request, "userlogin.html", {"message": msg})


def userchangepwd(request):
    useremail=request.session["auname"]
    return render(request,"userchangepwd.html",{"useremail" : useremail})

def userupdatepwd(request):
    useremail=request.session["auname"]
    opwd=request.POST["opwd"]
    npwd = request.POST["npwd"]
    print(useremail,opwd,npwd)

    flag=User.objects.filter(Q(email=useremail)&Q(password=opwd))
    if flag:
        print("old password is correct")
        User.objects.filter(email=useremail).update(password=npwd)
        print("updated successfully")
        msg="password updated successfully"
    else:
        print("old password is invalid")
        msg = "old password is incorrect"
    return render(request,"userchangepwd.html",{"useremail":useremail,"message":msg})


def contactmail(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        comment=request.POST['comment']
        email=request.POST['email']
        subject="If you have any query regarding Online donation"
        comment1=comment+" This is system generated mail do not respond to this mail"
        data=usercontact(firstname=firstname,lastname=lastname,comment=comment,email=email)
        data.save()
        send_mail(
            subject,
            comment1,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
        )
        return HttpResponse("<h1 align=center>Mail Sent Successfully</h1>")
    return render(request,"feedback.html")

def feedback(request):
    return render(request,"feedback.html")