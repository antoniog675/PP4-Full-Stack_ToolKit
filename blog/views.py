from django.shortcuts import render
from django.views import generic
from .models import Post
from django.http import HttpResponse

# Create your views here.


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


def explore(request):
    return HttpResponse('explore page')
    
# class PostDrafts

# class PostFavourites
