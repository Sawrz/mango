from django.urls import path
from django.conf import settings
from . import views

app_name = 'main'

if settings.LAUNCHED:
    indexView = views.MaintenanceView
else:
    indexView = views.SoonView

urlpatterns = [
    path('', indexView.as_view(), name='home'),
]
