from django.core.validators import RegexValidator
from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Shop(TimestampedModel):
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to="shop/Shop/%Y/%m/%d")
    telephone = models.CharField(max_length=14,
                                 validators=[
                                     RegexValidator(r"^\d{3,4}-?\d{3,4}-?\d{4}$", message="전화번호를 입력해주세요."),
                                 ],
                                 help_text="입력예시) 050-1234-5678")
    tag_set = models.ManyToManyField('Tag', blank=True)

    def __str__(self) -> str:
        return self.name


class Review(TimestampedModel):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=10)
    message = models.TextField()


class Tag(TimestampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name
