from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.translation import gettext as _
from django.conf import settings

@shared_task
def send_welcome_email(recipient, name, last_name):
    subject = _("Bienvenido/a a Nuestra Aplicación")
    message = render_to_string('email/welcome.html', {'name': name, 'last_name': last_name})
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [recipient],
        fail_silently=False,
        html_message=message,
    )