from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, TopicListCreateView, TopicDetailView, PostListCreateView, \
                    PostDetailView, CommentListCreateView, CommentDetailView
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path, include, re_path

urlpatterns = [
    # Маршруты для регистрации логина
    path('register/', RegisterView.as_view(), name='register'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # CRUD для тем
    path('topics/', TopicListCreateView.as_view(), name='topic_list_create'),
    path('topics/<int:pk>/', TopicDetailView.as_view(), name='topic_detail'),

    # CRUD для постов
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

    #  CRUD для комментариев
    path('comments/', CommentListCreateView.as_view(), name='comments-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comments-detail'),

    # Через видео

]