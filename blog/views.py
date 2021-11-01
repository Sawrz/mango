from django.views import generic
from .models import Post
from django.urls import reverse
from django.shortcuts import redirect
from datetime import datetime
import pytz


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

    def get(self, request, *args, **kwargs):
        if self.show_view():
            return super(PostDetailView, self).get(request, *args, **kwargs)
        else:
            return redirect(reverse('blog:posts'))

    def show_view(self):
        post = self.get_object()

        return post.published and datetime.now(tz=pytz.UTC) >= post.publish_date.replace(tzinfo=pytz.UTC)
