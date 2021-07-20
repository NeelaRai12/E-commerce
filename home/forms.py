from django import forms
from django import CountryField

class CheckoutForm(forms.Form):
    user_name = forms.CharField()
    address = forms.CharField()
    country = CountryField(blank_label='(select country)')
    zip = forms.CharField()
    payment_options = forms.BooleanField(widget=forms.CheckboxSelect())


