from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to='main/avatar')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class SocialMediaProfile(models.Model):
    class Meta:
        verbose_name = 'Social Media Profile'
        verbose_name_plural = 'Social Media Profiles'

    name = models.CharField(max_length=255, blank=False, null=False)
    url = models.URLField(max_length=255, blank=False, null=False)
    icon = models.FileField(null=False, upload_to='main/social_media')

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Media(models.Model):
    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Media Files'
        ordering = ['name']

    image = models.ImageField(blank=True, null=True, upload_to='main/media')
    url = models.URLField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False

        super(Media, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
