from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Testimonial, Certificate, TechnicalSkill, TechnicalSubskill
from blog.models import Post
from portfolio.models import Project


# Create your views here.
class SoonView(generic.TemplateView):
    template_name = 'main/soon.html'


class MaintenanceView(generic.TemplateView):
    template_name = 'main/maintenance.html'


class ResumeView(generic.TemplateView):
    template_name = 'resume/index.html'

    def get_context_data(self, **kwargs):
        context = super(ResumeView, self).get_context_data(**kwargs)

        testimonials = Testimonial.objects.filter(is_active=True).order_by('-date_added')
        certificates = Certificate.objects.filter(is_active=True).order_by('-date_received')
        posts = Post.released_objects.order_by('-publish_date')[:6]
        projects = Project.objects.filter(published=True, category='data analysis').order_by('-publish_date')[:3]

        context['testimonials'] = testimonials
        context['certificates'] = certificates
        context['posts'] = posts
        context['projects'] = projects

        return context


class TechnicalSkillView(generic.DetailView):
    model = TechnicalSkill
    template_name = 'resume/technical_skills_index.html'

    def get_context_data(self, **kwargs):
        context = super(TechnicalSkillView, self).get_context_data(**kwargs)

        skill = self.get_object()

        context['sub_skills'] = TechnicalSubskill.objects.filter(technical_skill__id=skill.id).order_by('-weight',
                                                                                                        '-score',
                                                                                                        'name')

        return context


class CertificatesView(generic.ListView):
    model = Certificate
    template_name = 'resume/certificates_index.html'
    context_object_name = 'certificates'
    queryset = Certificate.objects.filter(is_active=True).order_by('-date_received')


class CreatorLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('main:dashboard')


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
