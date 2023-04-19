from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Snippets
from .serializers import SnippetSerializer
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class SnippetListCreateAPIView(ListCreateAPIView):
    queryset = Snippets.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Snippets.objects.all()
    serializer_class = SnippetSerializer


@api_view(['GET', 'POST'])
def snippets_list(request, format=None):
    if request.method == 'GET':
        snippets_list = Snippets.objects.all()
        serializer = SnippetSerializer(snippets_list, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    snippet = get_object_or_404(Snippets.objects.all(), pk=pk)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=HTTP_204_NO_CONTENT)
