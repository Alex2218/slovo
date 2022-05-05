from celery import shared_task
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
# from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Header
from django.conf import settings
import logging
import os
import sys

from django.core.mail import EmailMessage

from django.core.mail import send_mail
@shared_task
def send_email_task(*args, **kwargs):
    print('send_email_task send_email_task ', kwargs['to_emails'])
    mail_subject = 'Пітвердження пошти для реєстрації.'
    try:
        send_mail(kwargs['mail_subject'] , kwargs['html_content'] , settings.EMAIL_HOST_USER , kwargs['to_emails'])
        print('no error! ' , kwargs['mail_subject'] , kwargs['html_content'] , settings.EMAIL_HOST_USER , kwargs['to_emails'])
        # email = EmailMessage(kwargs['mail_subject'], kwargs['html_content'], to=kwargs['to_emails'])
    except KeyError as e:
        print('error ' , e)
        send_mail(mail_subject, kwargs['html_content'] , settings.EMAIL_HOST_USER , kwargs['to_emails'])
        print(mail_subject, kwargs['html_content'] , settings.EMAIL_HOST_USER , kwargs['to_emails'])

        # email = EmailMessage(mail_subject, kwargs['html_content'], to=kwargs['to_emails'])
    # email.send()

    # from_email = settings.DEFAULT_FROM_EMAIL
    # message = Mail(
    #     from_email=from_email,
    #     **kwargs
    # )
    # message.add_header(Header('reply_to', 'uchetsmartlead@gmail.com'))
    #
    # try:
    #     sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
    #     sg.send(message)
    # except Exception as e:
    #     print(e.args)
