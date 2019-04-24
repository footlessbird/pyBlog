from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# UserCreationForm 으로부터 상속받음
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # email 필드 추가

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # form 에 보여질 필드


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
