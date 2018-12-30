from django.shortcuts import render
from django.views import generic
import markdown

from .models import Blog


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.all()

class DetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/stackedittextarea.html'
