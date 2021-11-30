from django.contrib import admin
from catblog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["cat_name", "cat_weight", "cat_healthy", "created_at"]
    search_fields = ["cat_name", "cat_character"]


admin.site.register(Post, PostAdmin)
