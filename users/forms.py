""" Forms  profile. """
""" Este tipo de forms es uno de los ma complejos"""

# Django
from django import forms
# model
from .models import User, Profile

class ProfileForm(forms.Form):
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()


class SignupForm(forms.Form):
    """ SingUp form"""
    username =  forms.CharField(min_length=5, max_length=50)
    password = forms.CharField(max_length=140, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=140, widget=forms.PasswordInput())
    first_name =  forms.CharField(min_length=2, max_length=255)
    last_name = forms.CharField(min_length=2, max_length=255)
    email = forms.CharField(min_length=6, max_length=70, widget=forms.EmailInput())

    """ Methodos de validacion """
    def clean_username(self):
        """ Username must be unique """
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username esta en uso')
        return username
    
    def clean(self):
        """ verify password confirmation match,"""
        data = super().clean()
        password = data['password']
        password_confirmation =  data['password_confirmation']

        if password !=  password_confirmation:
            raise forms.ValidationError('Los password estan incorrrectos')
        
        return data
    
    def save(self):
        """ create user and profile """
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()

        
