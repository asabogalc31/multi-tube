from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationFormFull(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Correo es requerido')
    first_name = forms.Field(required=True, help_text='Nombre es requerido')
    last_name = forms.Field(required=True, help_text='Apellido es requerido')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya esta en uso')
        return email
