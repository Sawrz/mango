from django.db import models


# Create your models here.
class Project(models.Model):
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['date_modified']

    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    url = models.URLField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    meta_description = models.CharField(max_length=150, blank=True)
    thumbnail = models.ImageField(blank=True, null=True, upload_to='portfolio/thumbnails')
    banner = models.ImageField(blank=True, null=True, upload_to='portfolio/banners')

    date_created = models.DateField(blank=False, null=False)
    date_modified = models.DateField(auto_now=True)
    show_up = models.BooleanField(default=True)
    actively_maintained = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/portfolio/{self.slug}'
