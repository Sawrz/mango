from django.views import generic
from .models import Blog


# Create your views here.
class BlogView(generic.ListView):
    model = Blog
    template_name = 'blog/index.html'
    paginate_by = 10

    def get_queryset(self):
        return super(BlogView, self).get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/post.html'
