from django.core.validators import MinLengthValidator
from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # 추상 클래스로서, DB 테이블이 생기지 않음.


class Post(TimestampedModel):
    author_name = models.CharField(max_length=20)
    title = models.CharField(
        max_length=200,
        db_index=True,
        validators=[
            MinLengthValidator(3),
            # MaxLengthValidator(),
        ],
    )
    content = models.TextField()
    photo = models.ImageField(upload_to="diary/post/%Y/%m/%d")
    tag_set = models.ManyToManyField("Tag", blank=True)
    ip = models.GenericIPAddressField()  # ip는 무조건 저장할것이기 때문에 필수 필드 = null

    def __str__(self) -> str:
        return f"[{self.pk}] {self.title}"

    class Meta:
        verbose_name = "포스팅"
        verbose_name_plural = "포스팅 목록"


class Comment(TimestampedModel):
    # 외래키 : 정수값
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self) -> str:
        return self.message

    class Meta:
        verbose_name = "댓글"
        verbose_name_plural = "댓글 목록"


class Tag(TimestampedModel):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "태그"
        verbose_name_plural = "태그 목록"
