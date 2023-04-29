from django.contrib import admin
from .models import Post, Like, Dislike


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author', 'created_date',)
    list_filter = ('author',)

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user',)
    list_filter = ('post',)


@admin.register(Dislike)
class DislikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user',)
    list_filter = ('post',)
