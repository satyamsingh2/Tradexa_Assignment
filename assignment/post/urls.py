from django.urls import path
from .views import UserView, PostDetailView, PostListView

urlpatterns = [
    path('user/', UserView.as_view(), name='user-list'),
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/<int:post_id>/', PostDetailView.as_view(), name='post-detail'),
]