from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Username"}))
    password = forms.CharField(
        max_length=200,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Enter password"}))


class TaskForm(forms.Form):
    task_id = forms.CharField(widget=forms.HiddenInput(), required=False)
    short_summary = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter short summary"}))
    url = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter url for task"}))
    long_summary = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Enter long summary"}))
