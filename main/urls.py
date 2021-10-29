from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolios'),
    path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name='project'),
    path('personal_site/', views.BlogView.as_view(), name='posts'),
    path('personal_site/<slug:slug>', views.BlogDetailView.as_view(), name='post'),
]
