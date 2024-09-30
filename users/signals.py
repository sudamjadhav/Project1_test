from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from requests import post

from .models import Profile


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()
    

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def send_registration_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to our platform.'
        message = f"Hi {instance.email},\n\nThank you for registering at our platform."
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [instance.email])
    else:
        subject = 'Your Profile has been Updated'
        message = f'Hi {instance.email},\n\nYour profile information has been successfully updated.'
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [instance.email])


@receiver(post_save, sender=Profile)
def send_mail_profile_updated(sender, instance, **kwargs):
    subject = 'Your Profile has been Updated'
    message = f'Hi {instance.user.email},\n\nYour profile information has been successfully updated.'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [instance.user.email])
                