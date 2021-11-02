from django.db import models


# Create your models here.
class ContactProfile(models.Model):
    class Meta:
        verbose_name = 'Contact Profile'
        verbose_name_plural = 'Contact Profiles'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name", max_length=255)
    email = models.EmailField(verbose_name='Email', max_length=255)
    message = models.TextField(verbose_name='Message', max_length=1000)

    def __str__(self):
        return f'{self.name}'
