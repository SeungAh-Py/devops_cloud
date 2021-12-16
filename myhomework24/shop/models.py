from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimestampedModel):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']


class Shop(TimestampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, db_index=True)
    photo = models.ImageField(upload_to="shop/shop/%Y/%m/%d")
    description = models.TextField()
    telephone = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(r"^\d{3,4}-?\d{3,4}-?\d{4}$")
        ],
        help_text="입력 예시) 042-1234-5678"
    )
    tag_set = models.ManyToManyField('Tag', blank=True)

    def get_absolute_url(self):
        return reverse("shop:shop_detail", args=[self.pk])

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["-id"]


class Review(TimestampedModel):
    post = models.ForeignKey(Shop, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.message

    class Meta:
        ordering = ["-id"]


class Tag(TimestampedModel):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]


