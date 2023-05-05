from django.urls import path, include
from .views import SnippetViewSet, UserViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from rest_framework.renderers import StaticHTMLRenderer

snippet_list = SnippetViewSet.as_view(
    {
        'get': 'list',
        'post': 'create'
    }
)

snippet_detail = SnippetViewSet.as_view(
    {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }
)

snippet_highlight = SnippetViewSet.as_view(
    {
        'get': 'highlight'
    },
    renderer_classes=[StaticHTMLRenderer]
)

user_list = UserViewSet.as_view(
    {
        'get': 'list'
    }
)

user_detail = UserViewSet.as_view(
    {
        'get': 'retrieve'
    }
)


router = DefaultRouter()
router.register(r'snippets', SnippetViewSet, basename='snippets')
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls))
]

urlpatterns += format_suffix_patterns(urlpatterns)
