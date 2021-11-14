from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


# Create your views here.
class SoonView(generic.TemplateView):
    template_name = 'main/soon.html'


class MaintenanceView(generic.TemplateView):
    template_name = 'main/maintenance.html'


class CreatorLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('create:dashboard')


class CreatorLogoutView(LogoutView):
    template_name = 'registration/logout.html'
