from .models import Testimonial, Certificate
from portfolio.models import Portfolio
from blog.models import Post
from django.views import generic


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        blogs = Post.objects.filter(published=True)
        portfolio = Portfolio.objects.filter(is_active=True)

        context['testimonials'] = testimonials
        context['certificates'] = certificates
        context['posts'] = blogs
        context['portfolio'] = portfolio

        return context
