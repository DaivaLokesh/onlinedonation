from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit
from adminmodule.models import Donation
class DonationPayment(forms.ModelForm):
    class Meta:
        model=Donation
        fields="__all__"

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper=FormHelper()
        self.helper.layout=Layout(
            "name",
            "amount",
            Submit('submit','Donate',css_class="button white btn-block btn-primary")
        )