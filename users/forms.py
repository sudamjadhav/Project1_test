from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser, Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].disabled = True

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user','bio','profile_picture','mobile','website',]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            


        