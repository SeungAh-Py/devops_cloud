from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from shop.forms import ShopForm, ReviewForm
from shop.models import Shop, Review

shop_list = ListView.as_view(
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
