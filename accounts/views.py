from django.shortcuts import render
from .forms import SignUpForm

# Create your views here.
def signup(request):
    user_form = SignUpForm()
    return render(request, 'registration/signup.html', {'user_form':user_form})