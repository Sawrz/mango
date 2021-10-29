from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


# Create your models here.
class Skill(models.Model):
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    name = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to='skills')
    is_key_skill = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to='avatar')
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to='cv')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'





class Testimonial(models.Model):
    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        ordering = ['name']

    thumbnail = models.ImageField(blank=True, null=True, upload_to='testimonials')
    name = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    quote = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Media(models.Model):
    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Media Files'
        ordering = ['name']

    image = models.ImageField(blank=True, null=True, upload_to='media')
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False

        super(Media, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolio Profiles'
        ordering = ['name']

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='portfolio')
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/portfolio/{self.slug}'


class Blog(models.Model):
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog Profiles'
        ordering = ['timestamp']

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='personal_site')
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

            super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/personal_site/{self.slug}'


class Certificate(models.Model):
    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
