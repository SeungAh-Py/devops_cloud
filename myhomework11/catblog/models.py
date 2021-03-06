from django.db import models


class Post(models.Model):
    cat_name = models.CharField(max_length=10)
    place_origin = models.CharField(max_length=10)
    cat_weight = models.CharField(max_length=11)
    cat_info = models.TextField(verbose_name="기본정보")
    cat_healthy = models.BooleanField(verbose_name="건강 양호")
    cat_character = models.TextField(verbose_name="성격")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(blank=True, upload_to='blog/post/%Y/%m/%d/%H')
