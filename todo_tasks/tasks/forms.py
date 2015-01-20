from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Username", 'required': ''}))
    password = forms.CharField(
        max_length=200,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Enter password", 'required': ''}))


class SignupForm(forms.Form):
    username = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Username", 'required': ''}))
    password = forms.CharField(
        max_length=200,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Enter password", 'required': ''}))
    confirm_password = forms.CharField(
        max_length=200,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Confirm password", 'required': ''}))
    email = forms.CharField(
        max_length=200,
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': "Enter email", 'required': '', 'equalto': "#id_password"}))


class TaskForm(forms.Form):
    task_id = forms.CharField(widget=forms.HiddenInput(), required=False)
    short_summary = forms.CharField(
        max_length=100,
        error_messages={'required': 'Enter short summary'},
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter short summary", 'required': ''}))
    url = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter url for task", 'required': ''}))
    long_summary = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Enter long summary", 'required': ''}))
