"""Models here are used to build the forms to get
data from the user"""
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Publish"))


class Post(models.Model):
    """Model to create a post for admin and user"""
    title = models.CharField(max_length=200, unique=True)
    spirit = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
        )
    featured_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True
        )

    class Meta:
        """Post will paginate in most recent posts first
        and older posts will be pushed back"""
        ordering = ["-created_on"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def _str_(self):
        return self.title

    def number_of_likes(self):
        """Counts the number of likes for each post"""
        return self.likes.count()


class Comment(models.Model):
    """This model is used to retrieve data used to build
    a comment form post"""
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
        )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """Oldest comments will be at the top, that way people
        can follow the conversation"""
        ordering = ['created_on']

    def __str__(self):
        return f"comment {self.body} by {self.name}"
