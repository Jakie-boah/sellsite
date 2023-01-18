from .models import UserProfile
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django.core.exceptions import ValidationError


class UserForm(forms.ModelForm):

    phone_number = PhoneNumberField(required=False)
    username = forms.CharField(max_length=50, label='Имя', required=False)
    usersurname = forms.CharField(max_length=50, label='Фамилия', required=False)
    email = forms.EmailField(error_messages={'invalid':"Допустили ошибку в email"})

    phone_number.error_messages['invalid'] = 'некорректно'

    class Meta:
        model = UserProfile
        fields = ['phone_number', 'username', 'usersurname', 'email']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number:
            raise ValidationError('Вы должны заполнить поля!')
        return phone_number

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise ValidationError('Вы должны заполнить поля!')
        return name

    def clean_usersurname(self):
        usersurname = self.cleaned_data.get('usersurname')
        if not usersurname:
            raise ValidationError('Вы должны заполнить поля!')
        return usersurname

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError('Вы должны заполнить поля!')
        return email


class LoginForm(forms.Form):
    login = forms.CharField(max_length=150, required=False, label='Логин')
    password = forms.CharField(max_length=150, required=False)
    def clean_login(self):
        login = self.cleaned_data.get('login')
        if not login:
            raise ValidationError('Вы должны заполнить поля!')
        return login

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise ValidationError('Вы должны заполнить поля!')
        return password









