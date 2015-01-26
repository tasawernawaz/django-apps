__author__ = 'Tasawer Nawaz'

from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField(required=False, max_length=50)


    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message.split()) < 4:
            raise forms.ValidationError ("Message length should be more than four words")
        return message
