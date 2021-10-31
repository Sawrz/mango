from django.views import generic
from .models import Post


# Create your views here.
class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['posts'] = Post.released_objects.all()

        return context


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'
