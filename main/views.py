from .models import Blog, Testimonial, Certificate
from portfolio.models import Portfolio
from django.views import generic


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)

        context['testimonials'] = testimonials
        context['certificates'] = certificates
        context['posts'] = blogs
        context['portfolio'] = portfolio

        return context








class BlogView(generic.ListView):
    model = Blog
    template_name = 'main/personal_site.html'
    paginate_by = 10

    def get_queryset(self):
        return super(BlogView, self).get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'main/personal_site-detail.html'
