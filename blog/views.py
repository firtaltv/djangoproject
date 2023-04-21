from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView, get_object_or_404,)
from django.shortcuts import render, redirect, reverse
from .models import Post, Like
from users.models import User
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_403_FORBIDDEN


class PostListAPIView(ListAPIView):
    queryset = Post.objects.order_by("published_date")
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return Response({'posts': self.get_queryset()}, template_name='blog/post_list.html')


def post_like(request, pk):
    post_inst = Post.objects.get(pk=pk)
    qs = Like.objects.filter(post__pk=pk, user__pk=request.user.pk)
    if not qs.exists():
        post_inst.like += 1
        post_inst.save()
        Like.objects.create(
            post=post_inst,
            user=User.objects.get(pk=request.user.pk)
        )
    return redirect('post_list')


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return Response({'post': self.object}, template_name='blog/post_detail.html')

    def get_object(self):
        qs = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(qs, pk=self.kwargs["pk"])
        return obj


class PostCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author__id=self.kwargs['pk'])

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Post.objects.create(
            author=serializer.validated_data['author'],
            text=serializer.validated_data['text'],
            title=serializer.validated_data['title'],
            published_date=serializer.validated_data['published_date'],
            created_date=serializer.validated_data['created_date'],
            like=serializer.validated_data['like']
        )
        return Response(serializer.data, status=HTTP_201_CREATED)


class PostDestroyAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user == instance.author:
            instance.delete()
            return Response(status=HTTP_200_OK)
        return Response(status=HTTP_403_FORBIDDEN)


class PostUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user == instance.author:
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(status=HTTP_403_FORBIDDEN)
