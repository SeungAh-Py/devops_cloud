from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from blog.models import Post


def index(request):
    return render(request, "blog/index.html")


def post_list(request: HttpRequest) -> HttpResponse:
    # request.GET   # QueryString Values
    # request.POST   # Post 요청 Values
    # request.FILES   # Post 요청에서 파일 Values

    qs = Post.objects.all()  # QuerySet Type (db 조회, sql에서 select all 과 같은..)
    qs = qs.order_by("-pk")  # order by (내림차순 정렬)

    q = request.GET.get("q", "")  # Query String / 하나의 사전으로 보면됨(request.GET)
    if q:
        qs = qs.filter(title__icontains=q)  # filter는 sql에서 where 조건과 같다고 보면 됨

    # blog/templates/blog/post_list.html
    return render(request, "blog/post_list.html", {
        "post_list": qs,
    })


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    # pk = 1
    post = Post.objects.get(pk=pk)
    return render(request, "blog/post_detail.html", {
        "post": post,
    })