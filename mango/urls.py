"""mango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('mango/', include('mango.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import CreatorLoginView, CreatorLogoutView

urlpatterns = []

if settings.MAINTENANCE or settings.DEBUG:
    patterns = [
        path('admin/', admin.site.urls),
    ]

    urlpatterns.extend(patterns)

if settings.MAINTENANCE:
    patterns = [
        path('', include('main.urls', namespace='main')),
    ]

    urlpatterns.extend(patterns)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.MAINTENANCE:
    patterns = [
        path('', include('resume.urls', namespace='resume')),
        path('login', CreatorLoginView.as_view(), name='login'),
        path('logout', CreatorLogoutView.as_view(), name='logout'),
        path('contact/', include('contact.urls', namespace='contact')),
        path('portfolio/', include('portfolio.urls', namespace='portfolio')),
        path('blog/', include('blog.urls', namespace='blog')),
    ]

    urlpatterns.extend(patterns)
