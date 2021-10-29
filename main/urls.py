from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('personal_site/', views.BlogView.as_view(), name='posts'),
    path('personal_site/<slug:slug>', views.BlogDetailView.as_view(), name='post'),
]
