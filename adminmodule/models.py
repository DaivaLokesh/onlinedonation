from django import forms
from django.db import models

# Create your models here.
class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,blank=False,unique=True)
    password=models.CharField(max_length=100,blank=False)

    class Meta:
        db_table="admin_table"

    def __str__(self):
        return self.username

class Donar(models.Model):
    id=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=100,blank=False)
    gender_choices=(("male","male"),("female","female"))
    gender=models.CharField(max_length=20,blank=False,choices=gender_choices)
    address=models.CharField(max_length=100,blank=False)
    state=models.CharField(max_length=100,blank=False)#states
    region_choices = (("INDIA", "INDIA"), ("Othercountry", "Othercountry"))  # tuple format
    region=models.CharField(max_length=100,blank=False,choices=region_choices)#india or other countries
    password=models.CharField(max_length=100,blank=False)
    email=models.CharField(max_length=100,blank=False,unique=True)
    contact= models.CharField(max_length=20,blank=False,unique=True)

    class Meta:
        db_table="donar_table"

    def __str__(self):
        return self.fullname

class User(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.BigIntegerField(blank=False, unique=True)
    fullname = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, blank=False)
    department_choices = (("NGO", "NGO"), ("ORPHANAGE", "ORPHANAGE"),("OLDAGEHOME","OLDAGEHOME"))
    department= models.CharField(max_length=100,blank=False,choices=department_choices )#NGO's,Orphanage,Childrens
    state = models.CharField(max_length=100, blank=False)  # states
    region = models.CharField(max_length=100, blank=False)  # india or other countries
    password = models.CharField(max_length=100, blank=False, default="donar123")
    email = models.CharField(max_length=100, blank=False, unique=True)
    contact = models.CharField(max_length=20, blank=False, unique=True)

    class Meta:
        db_table="user_table"

    def __str__(self):
        return self.fullname

class Payment(models.Model):
    mappingid=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    donar=models.ForeignKey(Donar,on_delete=models.CASCADE)

    class Meta:
        db_table="payment"


class Donation(models.Model):
    name=models.CharField(max_length=255)
    amount=models.CharField(max_length=100)
    order_id=models.CharField(max_length=100,blank=True)
    raxorpay_payment_id=models.CharField(max_length=100,blank=True)
    paid=models.BooleanField(default=False)

    class Meta:
        db_table="donation"


class DonarSignupForm(forms.ModelForm):
    class Meta:
        model = Donar
        fields = ['fullname', 'gender', 'address', 'state', 'region', 'password', 'email', 'contact']



class usercontact(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    comment = models.TextField(max_length=255)
    email = models.EmailField(blank=False)

    class Meta:
        db_table = "feedback"