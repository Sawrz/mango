from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Common(models.Model):
    class Meta:
        abstract = True

    institution = models.CharField(max_length=255, null=False)
    title = models.CharField(max_length=63, null=False)

    description = models.TextField(max_length=512, blank=True, null=True)
    is_active = models.BooleanField(default=True)


class Education(Common):
    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.title} - {self.institution}'


class Degree(Education):
    class Meta:
        verbose_name = 'Degree'
        verbose_name_plural = 'Degrees'
        ordering = ['-date_finished', 'institution']

    date_started = models.DateField(blank=False, null=False)
    date_finished = models.DateField(blank=True, null=True)

    major = models.CharField(max_length=63, blank=False, null=False)


class Certificate(Education):
    class Meta:
        verbose_name = 'Certification'
        verbose_name_plural = 'Certifications'
        ordering = ['-date_received', 'institution']

    date_received = models.DateField(blank=False, null=False)
    valid_until = models.DateField(blank=True, null=True)

    url = models.URLField(max_length=255, blank=True, null=True)


class WorkExperience(Common):
    class Meta:
        verbose_name = 'Work Experience'
        verbose_name_plural = 'Work Experiences'

    date_started = models.DateField(blank=False, null=False)
    date_finished = models.DateField(blank=True, null=True)
    department = models.CharField(max_length=255, blank=False, null=False)


class Language(models.Model):
    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    name = models.CharField(max_length=63, null=False, unique=True, blank=False)

    NO = 'no proficiency'
    ELEMENTARY = 'elementary proficiency'
    LIMITED_WORKING = 'limited working proficiency'
    PROFESSIONAL_WORKING = 'professional working proficiency'
    FULL_PROFESSIONAL = 'full professional working proficiency'
    NATIVE = 'native proficiency'
    PROFICIENCY = [
        (NO, 'No'),
        (ELEMENTARY, 'Elementary'),
        (LIMITED_WORKING, 'Limited Working'),
        (PROFESSIONAL_WORKING, 'Professional Working'),
        (FULL_PROFESSIONAL, 'Full Professional'),
        (NATIVE, 'Native'),
    ]
    proficiency = models.CharField(max_length=32, choices=PROFICIENCY, blank=False, null=False, default=NO)


class TechnicalSkill(models.Model):
    class Meta:
        verbose_name = 'Technical Skill'
        verbose_name_plural = 'Technical Skills'
        ordering = ['-score', 'name']

    name = models.CharField(max_length=255, null=False, unique=True)
    score = models.PositiveIntegerField(default=0, null=False, blank=False)
    is_active = models.BooleanField(default=True)

    slug = models.SlugField(max_length=255, unique=True, null=False)

    def __str__(self):
        return self.name


class TechnicalSubskill(models.Model):
    class Meta:
        verbose_name = 'Technical Subskill'
        verbose_name_plural = 'Technical Subskills'
        ordering = ['-weight', '-score', 'name']

    technical_skill = models.ForeignKey(TechnicalSkill, blank=False, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, unique=True)
    score = models.PositiveIntegerField(default=80, validators=[MinValueValidator(0), MaxValueValidator(100)],
                                        null=False, blank=False)
    weight = models.PositiveIntegerField(default=10, validators=[MinValueValidator(0), MaxValueValidator(10)],
                                         null=False, blank=False)

    def __str__(self):
        return self.name


class SoftSkill(models.Model):
    class Meta:
        verbose_name = 'Soft Skill'
        verbose_name_plural = 'Soft Skills'
        ordering = ['name']

    name = models.CharField(max_length=255, null=False, unique=True)
    icon = models.FileField(null=False, upload_to='resume/skills/soft')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class VoluntaryActivity(models.Model):
    pass


class Media(models.Model):
    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Media Files'
        ordering = ['name']

    image = models.ImageField(blank=True, null=True, upload_to='core/media')
    url = models.URLField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False

        super(Media, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Profile(models.Model):
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to='core/avatar')
    bio = models.TextField(blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    technical_skills = models.ManyToManyField(TechnicalSkill, blank=True)
    soft_skills = models.ManyToManyField(SoftSkill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to='resume/cv')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class SocialMediaProfile(models.Model):
    class Meta:
        verbose_name = 'Social Media Profile'
        verbose_name_plural = 'Social Media Profiles'

    name = models.CharField(max_length=255, blank=False, null=False)
    url = models.URLField(max_length=255, blank=False, null=False)
    icon = models.FileField(null=False, upload_to='core/social_media')

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Testimonial(models.Model):
    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        ordering = ['-date_added']

    thumbnail = models.ImageField(blank=True, null=True, upload_to='resume/testimonials/thumbnails')

    first_name = models.CharField(max_length=255, blank=True, null=False)
    last_name = models.CharField(max_length=255, blank=True, null=False)
    role = models.CharField(max_length=255, blank=True, null=False)
    profile_url = models.URLField(max_length=255, blank=True, null=True)

    quote = models.CharField(max_length=512, blank=True, null=False)

    date_added = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
