from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

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


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['country', 'city', 'photo']
        widgets = {
            'country':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Pais'}),
            'city': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Ciudad'}),
            'photo': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
        }
        labels={
            'country':'Pais',
            'city': 'Ciudad',
            'photo': 'Foto'
        }

class UserEditForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text='Correo es requerido')
    first_name = forms.Field(required=True, help_text='Nombre es requerido')
    last_name = forms.Field(required=True, help_text='Apellido es requerido')
    username = forms.Field(required=True, help_text='Nombre de usuario es requerido')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('El email ya esta en uso')
        return email
