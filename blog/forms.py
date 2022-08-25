from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class PostDrinkForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'spirit', 'ingredients', 
        'instructions', 'featured_image', 'status')