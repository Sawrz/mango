from django.views import generic
from .models import SoftwareProject, DataAnalysis
from django.http import Http404
from .models import DataAnalysis, SoftwareProject


# Create your views here.
class PortfolioView(generic.TemplateView):
    template_name = 'portfolio/index.html'

    def get_context_data(self, **kwargs):
        context = super(PortfolioView, self).get_context_data(**kwargs)

        data_analyses = DataAnalysis.objects.filter(published=True)
        software_projects = SoftwareProject.objects.filter(published=True)

        context['data_analyses'] = data_analyses[:2]
        context['software_projects'] = software_projects[:2]

        return context


class ProjectListView(generic.ListView):
    paginate_by = 10

    def get_queryset(self):
        return super(ProjectListView, self).get_queryset().filter(published=True)


class DataAnalysesView(ProjectListView):
    model = DataAnalysis
    template_name = 'portfolio/data_analyses_index.html'


class SoftwareProjectsView(ProjectListView):
    model = SoftwareProject
    template_name = 'portfolio/software_projects_index.html'


class ProjectDetailView(generic.DetailView):
    template_name = 'portfolio/project.html'

    def get(self, request, *args, **kwargs):
        project = self.get_object()

        if project.published:
            return super(ProjectDetailView, self).get(request, *args, **kwargs)
        else:
            raise Http404


class DataAnalysisDetailView(ProjectDetailView):
    model = DataAnalysis


class SoftwareProjectDetailView(ProjectDetailView):
    model = SoftwareProject
