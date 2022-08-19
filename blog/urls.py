from . import views
from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path('', views.home, name='home'),
    path('explore/', views.PostList.as_view(), name='explore'),
    path('<slug:slug>/', views.DrinksDetail.as_view(), name='drinks_detail')
]