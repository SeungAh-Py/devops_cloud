from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from catblog.models import Post


def index(request):
    return render(request, "catblog/index.html")


def post_list(request: HttpRequest) -> HttpResponse:
    # request.GET
    # request.POST
    # request.FILES

    qs = Post.objects.all()
    qs = qs.order_by("-pk") # 내림차순

    q = request.GET.get("q", "")
    if q:
        qs = qs.filter(title__icontains=q)

    # catblog/templates/catblog/post_list.html
    return render(request, "catblog/post_list.html", {
        "post_list": qs,
    })


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(pk=pk)
    return render(request, "catblog/post_detail.html", {
        "post": post,
    })

