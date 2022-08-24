from .models import Comment, PostDrink
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class PostDrinkForm(forms.ModelForm):
    class Meta:
        model = PostDrink
        fields = '__all__'