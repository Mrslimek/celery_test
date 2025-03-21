from celery import shared_task
import time
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def my_first_task():
    time.sleep(10)
    print('ТАСКА РАБОТАЕТ')
    return 100


@shared_task
def send_email_task():
    subject = 'Тема письма'
    message = 'Текст письма'
    recipient_list = ['viktorreentovich@yandex.ru']

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        recipient_list,
        fail_silently=False
    )
    return 'email отправлен'