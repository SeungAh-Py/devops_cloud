from django import forms

from shop.models import Shop


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        field = "__all__"
