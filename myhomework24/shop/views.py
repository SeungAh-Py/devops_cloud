from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from shop.forms import ShopForm, ReviewForm
from shop.models import Shop, Review


class ShopListView(ListView):
    model = Shop

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("query", "").strip()
        if query:
            qs = qs.filter(name__icontains=query)
        return qs


shop_list = ShopListView.as_view(
    model=Shop
)

shop_detail = DetailView.as_view(
    model=Shop
)

shop_new = CreateView.as_view(
    model=Shop,
    form_class=ShopForm,
)

shop_edit = UpdateView.as_view(
    model=Shop,
    form_class=ShopForm,
)

shop_delete = DeleteView.as_view(
    model=Shop,
)

review_new = CreateView.as_view(
    model=Review,
    form_class=ReviewForm,
)

review_edit = UpdateView.as_view(
    model=Review,
    form_class=ReviewForm,
)

review_delete = DeleteView.as_view(
    model=Review,
    success_url=reverse_lazy("shop:shop_list")
)
