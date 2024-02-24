from celery import shared_task
from A.utils import send_verify_email

@shared_task
def send_email(email,code):
    """
    get code like 12345 and email like email@example.com and send email with celery
    """
    return send_verify_email(user_email=email,code=code)