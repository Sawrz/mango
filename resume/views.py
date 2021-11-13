from .models import Testimonial, Certificate
from portfolio.models import Project
from blog.models import Post
from django.views import generic


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'resume/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        testimonials = Testimonial.objects.filter(is_active=True).order_by('-date_added')
        certificates = Certificate.objects.filter(is_active=True).order_by('-date_received')
        posts = Post.released_objects.order_by('-publish_date')[:2]
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
