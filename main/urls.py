from django.urls import path
from django.conf import settings
from . import views
import blog.views as blog_views

app_name = 'main'

if settings.MAINTENANCE:
    if settings.LAUNCHED:
        indexView = views.MaintenanceView
    else:
        indexView = views.SoonView
else:
    indexView = views.ResumeView

urlpatterns = [
    path('', indexView.as_view(), name='home'),
    path('login', views.CreatorLoginView.as_view(), name='login'),
    path('logout', views.CreatorLogoutView.as_view(), name='logout'),
    path('technical-skills/<slug:slug>', views.TechnicalSkillView.as_view(), name='technical_skill'),
    path('certificates', views.CertificatesView.as_view(), name='certificates'),
    path('creator', views.DashboardView.as_view(), name='dashboard'),
    path('creator/blog/create', blog_views.PostCreateView.as_view(), name='create_post'),
    path('creator/blog/<slug:slug>', blog_views.PostUpdateView.as_view(), name='update_post'),

]
