from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('explore/', views.PostList.as_view(), name='explore'),
    path('add_drinks/', views.CreateRecipeView.as_view(), name='add_drinks'),
    path('add_drinks/edit/<int:pk>', views.UpdatePostView.as_view(), name='edit_drinks'),
    path('add_drinks/<int:pk>/delete', views.DeletePostView.as_view(), name='delete_drinks'),
    path('drinks_favourites/', views.PostFavourites.as_view(), name='favourites'),
    path('drinks_favourites/<slug:slug>/', views.PostFavourites.as_view(), name='post_favourites'),
    path('<slug:slug>/', views.DrinksDetail.as_view(), name='drinks_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like')
]