from django.views import generic
from .models import Project
from django.urls import reverse
from django.shortcuts import redirect


# Create your views here.
class PortfolioView(generic.ListView):
    model = Project
    template_name = 'portfolio/index.html'
    paginate_by = 10

    def get_queryset(self):
        return super(PortfolioView, self).get_queryset().filter(show_up=True)


class PortfolioDetailView(generic.DetailView):
    model = Project
    template_name = 'portfolio/project.html'

    def get(self, request, *args, **kwargs):
        project = self.get_object()

        if project.show_up:
            return super(PortfolioDetailView, self).get(request, *args, **kwargs)
        else:
            return redirect(reverse('portfolio:projects'))
