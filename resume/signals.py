from django.db.models.signals import post_save
from django.dispatch import receiver
from main.models import Profile as MainProfile
from . models import Profile


@receiver(post_save, sender=MainProfile)
def create_profile(sender, instance, created, **kwargs):
    if created:
        userprofile = Profile.objects.create(main_profile=instance)