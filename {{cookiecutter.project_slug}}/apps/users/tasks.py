# Create your tasks here

from celery import shared_task


@shared_task
def send_mail(x, y):
    return x + y
