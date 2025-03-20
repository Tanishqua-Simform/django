from django.dispatch import Signal, receiver
from django.core.mail import send_mail
from ToDo.settings import EMAIL_HOST_USER

email_signal = Signal()

@receiver(email_signal)
def handle_email_signal(sender, **kwargs):
    subject = kwargs.get('subject')
    message = kwargs.get('message')
    to_email = kwargs.get('to_email')
    print('Le signal fenk ke maara')
    # send_mail(subject, message, EMAIL_HOST_USER, to_email)
