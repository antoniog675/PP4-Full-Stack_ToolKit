from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, PostDrinkForm

# Create your views here.


def home(request):
    return render(request, 'index.html')

def add_drinks(request):
    form = PostDrinkForm(data=request.POST)
    if form.is_valid():
        author = form.save(commit=False)
        author.author = request.user
        author.save()
        return redirect('/explore')
    return render(request, 'add_drinks.html', {"form": form})


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'explore.html'
    paginate_by = 6


class DrinksDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            "drinks_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        
        else:
            comment_form = CommentForm()
        
        return render(
            request,
            "drinks_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
    

class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('drinks_detail', args=[slug]))


class PostFavourites(generic.ListView):
    model = Post
    template_name = 'drinks_favourites.html'
    paginate_by = 6
    context_object_name = 'post_favourites'

    def get_queryset(self):
        user = self.request.user
        queryset = user.blogpost_like.all()
        return queryset


class FavouritesDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            "drinks_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        
        else:
            comment_form = CommentForm()
        
        return render(
            request,
            "drinks_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
    

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    form_class = PostDrinkForm
    context_object_name = 'edit_drinks'
    success_url = '/explore/'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        curr_post = Post.objects.filter(id=self.get_object().id)
        if curr_post:
            ctx['pk'] = curr_post[0].id
        return ctx


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    context_object_name = 'delete_drinks'
    success_url = '/explore/'