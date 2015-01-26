__author__ = 'Tasawer Nawaz'

from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    contact_no = forms.CharField()
    city = forms.CharField()
    address = forms.CharField()
