from django.contrib import admin
from diary.models import Post, Comment, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author_name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
