from django.contrib import admin

from shop.models import Shop, Category, Tag, Review


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["author_name"]