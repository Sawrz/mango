from .models import Testimonial, Certificate
from portfolio.models import Project
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
        portfolio = Project.objects.filter(show_up=True)

        context['testimonials'] = testimonials
        context['certificates'] = certificates
        context['posts'] = posts[:2]
        context['portfolio'] = portfolio[:2]

        return context
