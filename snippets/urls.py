from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.api_root),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
    path('snippets/', views.SnippetListCreateAPIView.as_view(), name='snippets_list'),
    path('snippets/<int:pk>/', views.SnippetDetailAPIView.as_view(), name='snippet_detail'),
    path('users/', views.UserListAPIView.as_view(), name='user_snippets_list'),
    path('users/<int:pk>/', views.SnippetDetailAPIView.as_view(), name='user_snippets'),
]

urlpatterns += format_suffix_patterns(urlpatterns)
