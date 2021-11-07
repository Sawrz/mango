from django.views import generic

# Create your views here.
class SoonView(generic.TemplateView):
    template_name = 'main/soon.html'


class MaintenanceView(generic.TemplateView):
    template_name = 'main/maintenance.html'
