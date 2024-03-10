from django.db.models import Q
from django.shortcuts import render, redirect
from adminmodule.models import DonarSignupForm, Donar, User, Donation
from django.views.decorators.csrf import csrf_exempt
from donar.forms import DonationPayment
import razorpay

def signup(request):
    if request.method == 'POST':
        form = DonarSignupForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or login page
            message = "User added Successfully"
            return redirect('donarlogin',{"msg":message})
    else:
        form = DonarSignupForm()
    return render(request, 'signup.html', {'form': form})


def donaruser(request):
    #donoremail=request.session["donoremail"]

    return render(request,"donaruser.html")


def donarlogin(request):
    return render(request,"donarlogin.html")

def donarchangepwd(request):
    donaremail=request.session["donoremail"]
    return render(request,"donarchangepwd.html",{"donaremail":donaremail})

def donorhome(request):
    donaremail=request.session["donoremail"]
    donar=Donar.objects.get(email=donaremail)
    return render(request,"donarhome.html",{"donaremail":donaremail,"donar":donar})

def donarupdatepwd(request):
    email=request.session["email"]
    opwd=request.POST["opwd"]
    npwd = request.POST["npwd"]
    print(email,opwd,npwd)

    flag=Donar.objects.filter(Q(email=email)&Q(password=opwd))
    if flag:
        print("old password is correct")
        Donar.objects.filter(email=email).update(password=npwd)
        print("updated successfully")
        msg="password updated successfully"
    else:
        print("old password is invalid")
        msg = "old password is incorrect"
    return render(request,"donarchangepwd.html",{"email":email,"message":msg})

def displaydonaruser(request):
    #donaremail=request.session["donaremail"]
    dept=request.POST["dept"]
    state=request.POST["state"]
    users=User.objects.filter(Q(department=dept)&Q(state=state))
    return render(request,"displaydonaruser.html",{"users":users})


def checkdonorlogin(request):
    email=request.POST["email"]
    pwd=request.POST["pwd"]

    flag=Donar.objects.filter(Q(email=email)&Q(password=pwd))
    print(flag)

    if flag:
        print("Login Success")
        request.session["donoremail"]=email
        donor = Donar.objects.get(email=email)
        return render(request,"donarhome.html",{"donor":donor})
    else:
        msg = "Login Failed"
        return render(request,"donarlogin.html",{"message":msg})

def donardonations(request):
    if request.method == "POST":
        name = request.POST['name']
        amount = int(request.POST['amount'])*100
        # create razorpay client object
        client = razorpay.Client(auth=("rzp_test_VfDnABLjynnWfn","Cm4F3ZNG7KyaHNAGEjG0UDMw"))
        # create order for the client
        response_payment = client.order.create(dict(
            amount = amount,
            currency = "INR"
        ))
        #print(response_payment)
        order_id = response_payment['id']
        payment_order_status = response_payment['status']
        if payment_order_status == 'created':
            donation = Donation(name=name,amount=amount,order_id=order_id)
            donation.save()
            response_payment['name'] = name
            form = DonationPayment(request.POST or None)
            return render(request,"donardonations.html",{"form":form,"payment":response_payment})
    form = DonationPayment()
    return render(request,'donardonations.html',{'form': form})

@csrf_exempt
def paymentstatus(request):
    response = request.POST
    print(response)
    return render(request,"payment_status.html")