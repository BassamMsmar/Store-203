from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

from .token import confirm_email_token_generator

def send_confirmation_email(request, user):
    token = confirm_email_token_generator.make_token(user)
    uid = user.id
    domain = get_current_site(request)

    subject = 'Activate your account'

    message = render_to_string(
        'registration/account-activation-email.html',
        {
            'user': user,
            'token': token,
            'domain': domain,
            'uid': uid
        }
    )

    user.email_user(subject, message)

