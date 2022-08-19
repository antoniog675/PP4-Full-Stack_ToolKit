from . import views
from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('explore/', views.explore),
]