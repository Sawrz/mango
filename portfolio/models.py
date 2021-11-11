from django.db import models


# Create your models here.
class Project(models.Model):
    class Meta:
        abstract = True
        ordering = ['-date_modified']

    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    url = models.URLField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    meta_description = models.CharField(max_length=150, blank=True)
    thumbnail = models.ImageField(blank=True, null=True, upload_to='portfolio/thumbnails')
    banner = models.ImageField(blank=True, null=True, upload_to='portfolio/banners')

    date_created = models.DateField(blank=False, null=False)
    date_modified = models.DateField(auto_now=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class SoftwareProject(Project):
    class Meta:
        verbose_name = 'Software Project'
        verbose_name_plural = 'Software Projects'

    actively_maintained = models.BooleanField(default=True)

    def get_absolute_url(self):
        return f'/portfolio/software-projects/{self.slug}'


class DataAnalysis(Project):
    class Meta:
        verbose_name = 'Data Analysis'
        verbose_name_plural = 'Data Analyses'

    def get_absolute_url(self):
        return f'/portfolio/data-analyses/{self.slug}'
