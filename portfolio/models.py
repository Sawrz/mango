from django.db import models


# Create your models here.
class Project(models.Model):
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        abstract = False
        ordering = ['-date_modified']

    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    url = models.URLField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    description = models.TextField(max_length=250, blank=True, null=True)
    meta_description = models.CharField(max_length=150, blank=True)
    thumbnail = models.ImageField(blank=True, null=True, upload_to='portfolio/thumbnails')
    banner = models.ImageField(blank=True, null=True, upload_to='portfolio/banners')

    SOFTWARE_PROJECT = 'software project'
    DATA_ANALYSIS = 'data analysis'
    CATEGORY = [
        (SOFTWARE_PROJECT, 'Software Project'),
        (DATA_ANALYSIS, 'Data Analysis'),
    ]
    category = models.CharField(max_length=32, choices=CATEGORY, blank=False, null=False)

    MAINTAINER = 'maintainer'
    CONTRIBUTOR = 'Contributor'
    ROLE = [
        (MAINTAINER, 'Maintainer'),
        (CONTRIBUTOR, 'Contributor')
    ]
    role = models.CharField(max_length=32, choices=ROLE, blank=False, null=False, default=MAINTAINER)

    date_created = models.DateField(blank=False, null=False)
    date_modified = models.DateField(auto_now=True)
    date_finished = models.DateField(blank=True, null=True)

    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/portfolio/{self.slug}'
