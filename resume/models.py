from django.db import models
from main.models import Profile as MainProfile
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class TechnicalSkill(models.Model):
    class Meta:
        verbose_name = 'Technical Skill'
        verbose_name_plural = 'Technical Skills'
        ordering = ['-score']

    name = models.CharField(max_length=255, null=False)
    score = models.PositiveIntegerField(default=80, validators=[MinValueValidator(0), MaxValueValidator(100)],
                                        null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class SoftSkill(models.Model):
    class Meta:
        verbose_name = 'Soft Skill'
        verbose_name_plural = 'Soft Skills'
        ordering = ['name']

    name = models.CharField(max_length=255, null=False)
    image = models.FileField(null=False, upload_to='resume/skills/soft')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    main_profile = models.OneToOneField(MainProfile, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    technical_skills = models.ManyToManyField(TechnicalSkill, blank=True)
    soft_skills = models.ManyToManyField(SoftSkill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to='resume/cv')

    def __str__(self):
        return f'{self.main_profile.user.first_name} {self.main_profile.user.last_name}'


class Testimonial(models.Model):
    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        ordering = ['-date_added']

    thumbnail = models.ImageField(blank=True, null=False, upload_to='resume/testimonials/thumbnails')

    first_name = models.CharField(max_length=255, blank=True, null=False)
    last_name = models.CharField(max_length=255, blank=True, null=False)
    role = models.CharField(max_length=255, blank=True, null=False)
    profile_url = models.URLField(max_length=255, blank=True, null=True)

    quote = models.CharField(max_length=512, blank=True, null=False)

    date_added = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Certificate(models.Model):
    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'

    title = models.CharField(max_length=255, null=False)
    institution = models.CharField(max_length=255, null=False)

    date_received = models.DateField(blank=False, null=False)
    valid_until = models.DateField(blank=True, null=True)

    description = models.CharField(max_length=512, blank=True, null=True)
    url = models.URLField(max_length=255, blank=True, null=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title} - {self.institution}'
