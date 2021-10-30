from django.views import generic
from .models import Post


# Create your views here.
class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = 10

    def get_queryset(self):
        return super(PostListView, self).get_queryset().filter(published=True)


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'
