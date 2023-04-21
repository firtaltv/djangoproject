from .models import Snippets
from .serializers import SnippetSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class SnippetListCreateAPIView(ListCreateAPIView):
    queryset = Snippets.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Snippets.objects.all()
    serializer_class = SnippetSerializer

