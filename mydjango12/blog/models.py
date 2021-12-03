from django.db import models
from blog.upload_to import uuid_name_upload_to


class Post(models.Model):
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    content = models.TextField()
    # upload_to
    # - 문자열을 지정하면 파일이 저장되는 폴더의 경로가 됨.
    photo = models.ImageField(blank=True, upload_to=uuid_name_upload_to) #'blog/post/%Y/%m/%d/%H')  # /%M/%S
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)