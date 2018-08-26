from .forms import UserCreationFormFull, ProfileForm, UserEditForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile
# Create your views here.

class SingUpView(CreateView):
    form_class = UserCreationFormFull
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SingUpView, self).get_form()
        form.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre'})
        form.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Apellido'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Correo electronico'})
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder':'Repetir contraseña'})
        return form


@method_decorator(login_required(), name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile


@method_decorator(login_required(), name='dispatch')
class userUpdate(UpdateView):
    form_class = UserEditForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/user_update_form.html'

    def get_object(self):
        return self.request.user

    def get_form(self, form_class=None):
        form = super(userUpdate, self).get_form()
        form.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre'})
        form.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Apellido'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Correo electronico'})
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder': 'Nombre de usuario'})
        return form