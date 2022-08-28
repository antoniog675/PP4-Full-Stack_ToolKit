"""Import AppConfig to create apps"""
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """Blog app created here"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
