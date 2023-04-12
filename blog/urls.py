from django.urls import path
from . import views


urlpatterns = [
    path('post/list/', views.PostListAPIView.as_view()),
    path('post/detail/<int:pk>', views.PostDetailAPIView.as_view(), name='post_detail'),
    path('post/create', views.PostCreateAPIView.as_view()),
    path('post/delete/<int:pk>', views.PostDestroyAPIView.as_view()),
    path('post/edit/<int:pk>', views.PostUpdateAPIView.as_view()),
]
