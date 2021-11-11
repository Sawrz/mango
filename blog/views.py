from django.views import generic
from .models import Post
from django.http import Http404


# Create your views here.
class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4
    queryset = Post.released_objects.all()


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'

    def get(self, request, *args, **kwargs):
        post = self.get_object()

        if post.published and post.released():
            return super(PostDetailView, self).get(request, *args, **kwargs)
        else:
            raise Http404
