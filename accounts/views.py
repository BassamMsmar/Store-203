from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponseBadRequest

from django.contrib.auth.models import User
from .token import confirm_email_token_generator

from .utils import send_confirmation_email

from .forms import SignUpForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.is_active = False
            user.save()
            send_confirmation_email(request, user)
            context = {
                    'user': user
                }
            return render(request, 'registration/signup-successful.html', context)
    else:
        user_form = SignUpForm()
        
    return render(request, 'registration/signup.html', {'user_form':user_form})


def activate_email(request, uid, token):
    user = get_object_or_404(User, pk=uid)
    if confirm_email_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        return redirect('login')
    
    else:
        return HttpResponseBadRequest('Bad token')


    