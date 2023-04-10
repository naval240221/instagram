from .models import *
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class NewPostForm(forms.ModelForm):
    class Meta:
        model = InstaPost
        fields = ['image', 'caption', 'location', 'hashtags']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'accept': 'image/*', 'class': 'form-control'}),
            'caption': forms.TextInput(attrs={'placeholder': 'Write a caption...', 'class': 'form-control'}),
            'location': forms.TextInput(attrs={'placeholder': 'Add a location...', 'class': 'form-control'}),
            'hashtags': forms.TextInput(attrs={'placeholder': 'Add some hashtags...', 'class': 'form-control'}),
        }


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["bio", "profile_pic", "profile_avatar", "date"]


class CustomLoginForm(AuthenticationForm):
    template_name = 'instaapp/home.html'
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # customize form fields as desired
        self.fields['username'].widget.attrs.update({
          'class': 'form-control',
          'placeholder': 'Enter your username here'
        })
        self.fields['password'].widget.attrs.update({
          'class': 'form-control',
          'placeholder': 'Enter your password'
        })
