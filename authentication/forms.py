from authentication.models import MyCustomUser
from django import forms


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = MyCustomUser
        fields = ['email', 'first_name', 'last_name', 'password']


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
