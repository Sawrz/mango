from django.db.models.signals import post_save
from django.dispatch import receiver
from main.models import Profile as MainProfile
from .models import Profile, TechnicalSkill, TechnicalSubSkill
import numpy as np


@receiver(post_save, sender=MainProfile)
def create_profile(sender, instance, created, **kwargs):
    if created:
        userprofile = Profile.objects.create(main_profile=instance)


def update_skill_score(technical_skill):
    sub_skills = TechnicalSubSkill.objects.filter(technical_skill__id=technical_skill.id, weight__gt=0).all()

    weights, scores = zip(*[(sub_skill.weight, sub_skill.score) for sub_skill in sub_skills])
    weights = np.exp(weights)

    max_total_points = sum(weights * 100)
    total_points = sum(map(lambda w, s: w * s, weights, scores))

    return total_points / max_total_points * 100


@receiver(post_save, sender=TechnicalSubSkill)
def update_technical_skill_score(sender, instance, **kwargs):
    technical_skill = TechnicalSkill.objects.get(id=instance.technical_skill.id)
    technical_skill.score = update_skill_score(technical_skill)
    technical_skill.save(update_fields=['score'])
