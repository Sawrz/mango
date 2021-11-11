from .models import Testimonial, Certificate
from portfolio.models import DataAnalysis, SoftwareProject
from blog.models import Post
from django.views import generic


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'resume/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        posts = Post.released_objects.all()
        data_analyses = DataAnalysis.objects.filter(published=True)
        software_projects = SoftwareProject.objects.filter(published=True)

        context['testimonials'] = testimonials
        context['certificates'] = certificates
        context['posts'] = posts[:2]
        context['data_analyses'] = data_analyses[:2]

        return context
