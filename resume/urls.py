from django.urls import path
from . import views

app_name = 'resume'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('technical-skills/<slug:slug>', views.TechnicalSkillView.as_view(), name='technical_skill'),
    path('certificates', views.CertificatesView.as_view(), name='certificates'),
]
