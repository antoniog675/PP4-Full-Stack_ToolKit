"""Building the admin page"""
from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """Post view for admin, there is filter to narrow down searches"""

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'ingredients']
    summernote_fields = ('ingredients', 'instructions')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin can approve comments that will go on website from here"""
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """Approve comments from here"""
        queryset.update(approved=True)
