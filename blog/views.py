from django.views import generic
from .models import Post
from main.views import CreateLoginRequired
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.text import slugify


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

        if post.published and post.released():
            return super(PostDetailView, self).get(request, *args, **kwargs)
        else:
            raise Http404


class PostCreateView(CreateLoginRequired, generic.CreateView):
    model = Post
    fields = ['title', 'subtitle', 'body', 'description', 'meta_description',
              'thumbnail', 'publish_date', 'published', 'author']
    template_name = 'blog/post_update_form.html'

    def get_success_url(self):
        return reverse_lazy('blog:posts')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.slug = slugify(f'{post.title} {post.subtitle}')
        post.save()

        return super(PostCreateView, self).form_valid(form)


class PostUpdateView(CreateLoginRequired, generic.UpdateView):
    model = Post
    fields = ['title', 'body', ]
    template_name = 'blog/post_update_form.html'

    def get_success_url(self):
        return reverse_lazy('blog:posts')
