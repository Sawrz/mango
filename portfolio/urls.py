from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.PortfolioView.as_view(), name='projects'),
    path('data-analyses', views.DataAnalysesView.as_view(), name='data-analyses'),
    path('data-analyses/<slug:slug>', views.DataAnalysisDetailView.as_view(), name='data-analysis'),
    path('software-projects', views.SoftwareProjectsView.as_view(), name='software-projects'),
    path('software-projects/<slug:slug>', views.SoftwareProjectDetailView.as_view(), name='software-project'),
]
