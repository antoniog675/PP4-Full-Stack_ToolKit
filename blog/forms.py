"""
These are the forms used for user comments, and if user
wishes to upload a drink the PostDrinkForm is used to
retrieve information to build the post
"""
from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """Comment Form  so users can comment on posts"""
    class Meta:
        """Meta for CommentForm"""
        model = Comment
        fields = ('body',)


class PostDrinkForm(forms.ModelForm):
    """PostDrinkForm for user to post drink"""
    class Meta:
        """Meta for PostDrinkForm"""
        model = Post
        fields = (
            "id", 'title', 'spirit', 'ingredients', 'instructions',
            'featured_image', 'status')
