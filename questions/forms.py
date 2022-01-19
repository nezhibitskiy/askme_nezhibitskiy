from django import forms
from questions.models import Question


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput()
    )


class RegisterForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput
    )
    nickname = forms.CharField(
        required=True
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
    )
    repeat_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
    )
    avatar = forms.FileField(
        allow_empty_file=False,
        widget=forms.FileInput,
        required=False
    )