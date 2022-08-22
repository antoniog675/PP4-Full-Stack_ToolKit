from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('explore/', views.PostList.as_view(), name='explore'),
    path('<slug:slug>/', views.DrinksDetail.as_view(), name='drinks_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like')
]