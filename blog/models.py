from django.db import models
from django.template.defaultfilters import slugify
from core.models import Profile
from datetime import datetime
import pytz


# Create your models here.
class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']

    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'

    category = models.ForeignKey(Category, blank=False, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class PostReleaseManager(models.Manager):
    def get_queryset(self):
        posts = super(PostReleaseManager, self).get_queryset().filter(published=True)
        post_ids = [p.id for p in posts if p.check_release_date()]

        return posts.filter(id__in=post_ids)


class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-publish_date']
        unique_together = ('title', 'subtitle')

    # Post Essentials
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    featured_image = models.ImageField(blank=True, null=True, upload_to='blog/featured_images')
    slug = models.SlugField(max_length=255, unique=True, null=False, blank=True)
    body = models.TextField(blank=True, null=True)

    # Presentation & SEO
    description = models.TextField(max_length=250, blank=True, null=True)
    meta_description = models.CharField(max_length=150, blank=True)
    thumbnail = models.ImageField(blank=True, null=True, upload_to='blog/thumbnails')

    # Status & Visibility
    publish_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(Profile, on_delete=models.PROTECT, blank=True)

    PUBLIC = 'public'
    PRIVATE = 'private'
    VISIBILITY = [
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private')
    ]
    visibility = models.CharField(max_length=32, choices=VISIBILITY, blank=False, null=False, default=PUBLIC)

    # Meta Information
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now=True)

    # Content Organization
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(SubCategory, blank=True, null=True, on_delete=models.PROTECT)

    # Managers
    objects = models.Manager()
    released_objects = PostReleaseManager()

    def __str__(self):
        if self.subtitle is not None:
            return f'{self.title}-{self.subtitle}'
        else:
            return self.title

    def check_release_date(self):
        return datetime.now(tz=pytz.UTC) >= self.publish_date.replace(tzinfo=pytz.UTC)

    def check_released(self):
        return self.check_release_date() and self.published

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(f'{self.title} {self.subtitle}')

        if self.publish_date is not None:
            self.published = True
        else:
            self.published = False

        super(Post, self).save(*args, **kwargs)
