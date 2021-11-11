from django.views import generic
from django.http import Http404
from .models import Project


# Create your views here.
class ProjectsListView(generic.ListView):
    model = Project
    paginate_by = 10
    template_name = 'portfolio/index.html'

    def get_queryset(self):
        return super(ProjectsListView, self).get_queryset().filter(published=True)

    def get_context_data(self, **kwargs):
        context = super(ProjectsListView, self).get_context_data(**kwargs)

        context['data_analyses'] = Project.released_objects.filter(category='data analysis')
        context['software_projects'] = Project.released_objects.filter(category='software project')

        return context


class ProjectDetailView(generic.DetailView):
    model = Project

    def get(self, request, *args, **kwargs):
        project = self.get_object()

        if project.published and project.released():
            return super(ProjectDetailView, self).get(request, *args, **kwargs)
        else:
            raise Http404


class DataAnalysisDetailView(ProjectDetailView):
    template_name = 'portfolio/data_analysis.html'


class SoftwareProjectDetailView(ProjectDetailView):
    template_name = 'portfolio/software_project.html'
