from django.shortcuts import render
from django.views import generic
from .models import Post
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'index.html')

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'explore.html'
    paginate_by = 6
    
# class PostDrafts

# class PostFavourites
