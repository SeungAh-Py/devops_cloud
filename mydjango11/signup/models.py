from django.db import models


class Bbs(models.Model):
    title = models.CharField(max_length=100, verbose_name="제목")
    name = models.CharField(max_length=100, verbose_name="이름")
    date = models.DateTimeField(verbose_name="작성시간")
    mobile = models.CharField(max_length=11, verbose_name="연락처")
    email = models.EmailField(verbose_name="이메일")
    context = models.TextField(verbose_name="내용")

    def __str__(self):
        return self.title
