from django.urls import path
from django.conf import settings
from . import views


if settings.LAUNCHED:
    indexView = views.MaintenanceView
else:
    indexView = views.SoonView

app_name = 'main'

urlpatterns = [
    path('', indexView.as_view(), name='home'),
]
