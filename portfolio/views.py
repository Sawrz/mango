from django.views import generic
from .models import Portfolio


# Create your views here.
class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = 'portfolio/index.html'
    paginate_by = 10

    def get_queryset(self):
        return super(PortfolioView, self).get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = 'portfolio/project.html'
