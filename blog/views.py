from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Posts, Comment
from django.views.generic import ListView, DetailView

def Text(request):
    return HttpResponse('egregergeg')

class PostListView(ListView):
    template_name = 'post_list.html'
    queryset = Posts.objects.all()
    context_object_name = 'post'


class PostDetailView(DetailView):
    queryset = Posts.objects.all()
    template_name = "blog_detail.html"
    context_object_name = "blog"

    def get_context_data(self, **kwargs):
        context: dict = super(PostDetailView, self).get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        comments: list[Comment] = Comment.objects.filter(post_id=pk)
        context["commnets"] = comments
        return context






























