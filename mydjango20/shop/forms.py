from django import forms
from shop.models import Shop, Tag


class ShopForm(forms.ModelForm):
    tags = forms.CharField()

    def save(self):
        # 부모의 save를 호출해 주어야 한다.
        saved_post = super().save()

        # 부가적인 연산을 수행할 수 있음
        tag_list = []
        tags = self.cleaned_data.get("tags", "")
        for word in tags.split(','):
            tag_name = word.strip()
            tag, __ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)

        saved_post.tag_set.clear()  # 간단구현을 위해 clear 호출
        saved_post.tag_set.add(*tag_list)

        return saved_post

    # 임의의 이름

    class Meta:
        model = Shop
        fields = [
            "category",
            "name",
            "telephone",
            "description",
        ]
