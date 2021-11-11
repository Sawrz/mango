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

        data_analyses = Project.objects.filter(published=True, category='data analysis')
        software_projects = Project.objects.filter(published=True, category='software project')

        context['data_analyses'] = data_analyses
        context['software_projects'] = software_projects

        return context


class ProjectDetailView(generic.DetailView):
    model = Project

    def get(self, request, *args, **kwargs):
        project = self.get_object()

        if project.published:
            return super(ProjectDetailView, self).get(request, *args, **kwargs)
        else:
            raise Http404


class DataAnalysisDetailView(ProjectDetailView):
    template_name = 'portfolio/data_analysis.html'


class SoftwareProjectDetailView(ProjectDetailView):
    template_name = 'portfolio/software_project.html'
