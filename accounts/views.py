from django.shortcuts import render, redirect
from .forms import SignUpForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect ('products')
    else:
        user_form = SignUpForm()
        
    return render(request, 'registration/signup.html', {'user_form':user_form})