from django.db import models
from django.template.defaultfilters import slugify
from main.models import Profile
from datetime import datetime
import pytz


# Create your models here.
class Tag (models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-publish_date']

    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    body = models.TextField(blank=True, null=True)
    meta_description = models.CharField(max_length=150, blank=True)
    thumbnail = models.ImageField(blank=True, null=True, upload_to='blog/thumbnails')
    banner = models.ImageField(blank=True, null=True, upload_to='blog/banners')

    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)

    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.title}-{self.subtitle}'

    def get_absolute_url(self):
        return f'/blog/{self.slug}'

    @property
    def is_due(self):
        return datetime.now(tz=pytz.UTC) >= self.publish_date.replace(tzinfo=pytz.UTC)

