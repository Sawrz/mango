from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.ProjectsListView.as_view(), name='projects'),
    path('data-analysis/<slug:slug>', views.DataAnalysisDetailView.as_view(), name='data_analysis'),
    path('software-project/<slug:slug>', views.SoftwareProjectDetailView.as_view(), name='software_project'),

]
