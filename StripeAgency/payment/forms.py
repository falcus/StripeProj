from django import forms

class PaymentForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    card_number = forms.CharField()
    exp_date = forms.CharField()
    cvc = forms.CharField()