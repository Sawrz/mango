from django.urls import path
from django.conf import settings
from . import views

app_name = 'core'

if settings.MAINTENANCE:
    if settings.LAUNCHED:
        indexView = views.MaintenanceView
    else:
        indexView = views.SoonView
else:
    indexView = views.ResumeView

urlpatterns = [
    path('', indexView.as_view(), name='home'),
    path('technical-skills/<slug:slug>', views.TechnicalSkillView.as_view(), name='technical_skill'),
    path('certificates', views.CertificatesView.as_view(), name='certificates'),
]
