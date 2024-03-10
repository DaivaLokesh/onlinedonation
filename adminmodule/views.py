from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect

from .models import Donar, User, Admin
from .forms import AddDonarForm

# Create your views here.
# def projecthomepage(request):
#     return render(request,'projecthomepage.html')
#
# def donarhomepage(request):
#     return render(request, 'donarhomepage.html')
#
# def userhomepage(request):
#     return render(request, 'userhomepage.html')

def adminhome(request):
    auname=request.session["auname"]
    return render(request,"adminhome.html",{"adminuname":auname})


def donarhome(request):
    #donaremail=request.session["donaremail"]
    return render(request,"donarhome.html")
                  #{"donaremail":donaremail})

def logout(request):

    return render(request,"login.html")



def checkadminlogin(request):
    adminuname=request.POST["uname"]
    adminpwd=request.POST["pwd"]

    flag=Admin.objects.filter(Q(username=adminuname)&Q(password=adminpwd))
    print(flag)

    if flag:
        print("Login Success")
        request.session["auname"]=adminuname
        return render(request,"adminhome.html",{"adminuname":adminuname})
    else:
        msg = "Login Failed"
        return render(request,"login.html",{"message":msg})

def viewdonars(request):
    donar=Donar.objects.all()
    count=Donar.objects.count()
    auname = request.session["auname"]
    return render(request,"viewdonars.html",{"donardata":donar,"count":count,"adminuname":auname})

def viewusers(request):

    users=User.objects.all()
    count = User.objects.count()
    auname = request.session["auname"]
    return render(request,"viewusers.html",{"userdata":users,"count":count,"adminuname":auname})

def adminuser(request):
    auname = request.session["auname"]
    return render(request,"adminuser.html",{"adminuname":auname})


def admindonar(request):
    auname = request.session["auname"]
    return render(request,"admindonar.html",{"adminuname":auname})

def adduser(request):
    auname=request.session["auname"]
    return render(request,"addusers.html",{"adminuname":auname})

def insertuser(request):

    if request.method=="POST":
        id=request.POST["id"]
        fname=request.POST["fname"]
        address= request.POST["address"]
        dept=request.POST["dept"]
        state=request.POST["state"]
        region=request.POST["region"]
        pas=request.POST["pas"]
        email=request.POST["email"]
        contact=request.POST["contact"]

        user=User(userid=id,fullname=fname,address=address,department=dept,state=state,region=region,password=pas,email=email,contact=contact)
        User.save(user)

        message="User added Successfully"
        return  render(request,"adduser.html",{"msg":message})

def deleteuser(request):

    users = User.objects.all()
    count = User.objects.count()
    return render(request, "deleteuser.html", {"userdata": users, "count": count})

def userdeletion(request,id):

    User.objects.filter(id=id).delete()

    return redirect("deleteuser")

def addDonar(request):
    #auname=request.session["auname"]
    auname = request.session["auname"]
    form=AddDonarForm()
    if request.method=="POST":
        form1=AddDonarForm(request.POST)
        if form1.is_valid():
            form1.save()
           # return HttpResponse("Donar added successfully")
            message="Donar added Successfully"
            return render(request,"adddonar.html",{"msg":message,"adminuname":auname})
        else:
            message="Fail to add Student"
            return render(request, "adddonar.html", {"msg": message, "adminuname": auname})


    return render(request,"addDonar.html",{"form":form})

def deletedonar(request):

    donars = Donar.objects.all()
    count = Donar.objects.count()
    return render(request, "deletedonar.html", {"donardata": donars, "count": count})

def donardeletion(request,id):

    Donar.objects.filter(id=id).delete()

    return redirect("deletedonar")

def payment(request):
    return render(request,"payment.html")


def adminchangepwd(request):
    auname = request.session["auname"]
    print(auname)
    return render(request,"adminchangepwd.html",{"adminuname":auname})
    #return HttpResponse("Admin change password page")

def adminupdatepwd(request):
    auname=request.session["auname"]
    opwd=request.POST["opwd"]
    npwd = request.POST["npwd"]
    print(auname,opwd,npwd)
    flag=Admin.objects.filter(Q(username=auname)&Q(password=opwd))
    if flag:
        print("old password is correct")
        Admin.objects.filter(username=auname).update(password=npwd)
        print("updated successfully")
        msg="password updated successfully"
    else:
        print("old password is invalid")
        msg = "old password is incorrect"
    return render(request,"adminchangepwd.html",{"adminuname":auname,"message":msg})


def usercontact(request):
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
        return HttpResponse("Mail Sent Successfully")
    return render(request,"usercontact.html")