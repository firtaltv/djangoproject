from django.urls import path
from . import views


urlpatterns = [
    path('', views.snippets_list),
    path('<int:pk>/', views.snippet_detail),
]
