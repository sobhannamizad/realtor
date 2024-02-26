from random import randint
from django.core.mail import EmailMessage
from rest_framework.permissions import BasePermission
from dotenv import load_dotenv
import os

load_dotenv()
class UserNotAuthenticated(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return False
        return True

def create_verify_code():
    """
    return a verify code like 12345
    """
    code = randint(10000,99999)
    return code

def send_verify_email(user_email,message,subject):
    """
    need a email target like example@example.com
    and send a verify code like 12345 to email
    """
    email = EmailMessage(
        subject,
        message,
        os.environ.get('GMAIL_USER'),
        [user_email],
        # reply_to=['another@example.com'],
        # headers={'Message-ID': 'foo'},
    )
    return email.send()

