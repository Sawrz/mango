from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from blog.models import Post
from portfolio.models import Project


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


class CreateLoginRequired(LoginRequiredMixin):
    login_url = reverse_lazy('login')
    redirect_field_name = 'login'


class DashboardView(CreateLoginRequired, generic.TemplateView):
    template_name = 'create/dashboard.html'


class PostCreateView(CreateLoginRequired, generic.CreateView):
    model = Post


class PostEditView(CreateLoginRequired, generic.UpdateView):
    model = Post
