from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_create, name='homepage'),
    path('new_post/', views.PostCreateView.as_view(), name='create_post'),
    path('edit_post/<int:pk>/', views.PostUpdateView.as_view(), name='edit_post'),
    path('view_post/<int:post_id>/', views.CommentCreateView.as_view(), name='view_post'),
    path('posts/mine/', views.my_posts, name='my_posts')
]