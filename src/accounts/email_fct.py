from django.core.mail import send_mail
from django.conf import settings

# send email function

def send_email_fct(email,token):
    from_adrss = settings.EMAIL_HOST_USER
    to_adrss = [email]
    subject = "reset your password"
    message = f"Hi,\n click on link to reset your massword http://127.0.0.1:8000/accounts/password_reset_form/{token}/"
    send_mail(subject,message,from_adrss,to_adrss)
    return True

    

