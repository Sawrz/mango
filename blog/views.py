from django.views import generic
from .models import Post
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = 4
    context_object_name = 'posts'

    def get_queryset(self):
        return self.model.released_objects.all()

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)

        posts = self.get_queryset()
        context['paginate_posts'] = posts.count() > self.paginate_by

        return context


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'

    def get(self, request, *args, **kwargs):
        post = self.get_object()

        if post.check_released():
            return super(PostDetailView, self).get(request, *args, **kwargs)
        else:
            raise Http404


class PostDetailPreview(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = 'blog/post.html'
