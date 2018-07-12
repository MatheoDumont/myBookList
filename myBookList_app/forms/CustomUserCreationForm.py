from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UniqueUserMail(forms.EmailField):
    def validate(self, value):
        super(forms.EmailField,self).validate(value)
        if User.objects.filter(email=value).exists():
            raise forms.ValidationError("L'émail n'existe pas")


class CustomUserCreationForm(UserCreationForm):
    email = UniqueUserMail()

    def __init__(self, *args, **kw):
        super(UserCreationForm, self).__init__(*args, **kw)

        super().order_fields(['username', 'email', 'password1', 'password2'])
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
        return user

