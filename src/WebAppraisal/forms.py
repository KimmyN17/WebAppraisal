from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from src.webapp.models import Profile

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=False)
    user_role = forms.ChoiceField(required=True, choices=Profile.Roles.choices)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2", "phone_number", "user_role")
