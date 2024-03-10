from django import forms
from .models import Donar

class AddDonarForm(forms.ModelForm):
    class Meta:
        model= Donar
        fields="__all__"#all fields in the model
        exclude={"password"}# this will exclude fields
        labels={"donarid":"Enter donar id","gender":"Select gender","fullname":"ENter Full Name","address":"Enter Address","region":"Select region"}