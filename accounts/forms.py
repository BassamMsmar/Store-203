from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length='30', required=False)
    last_name = forms.CharField(max_length='30', required=False)
    email = forms.EmailField(max_length='254', help_text='Required! Inform a valid email address')
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', )
