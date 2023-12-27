import profile
from django import forms
from django.contrib.auth.models import User
from apps.userprofile.models import Profile
from django.contrib.auth.forms import UserCreationForm


# USER FORM
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]


# USER ADD FORM
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]


# PROFILE FORM
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
            'phone',
            'birth_date',
            'bio',
            'avatar',
        ]
        # widgets = {
        #     'birth_date': forms.DateInput(
        #         attrs={'type': 'date',}
        #     )
        # }