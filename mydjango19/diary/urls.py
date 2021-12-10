from django.urls import path

from diary import views

app_name = 'diary'

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path("new/", views.post_new, name="post_new"),
    path("<int:pk>/edit/", views.post_edit, name="post_edit"),
    # 태그 클릭시 해당값 나오게 하는 것 구현2 (url)
    path("tags/<str:tag_name>/", views.tag_detail, name="tag_detail"),
    path("<int:post_pk>/comments/new/", views.comment_new, name="comment_new"),
    path("<int:post_pk>/comments/<int:pk>/edit/", views.comment_edit, name="comment_edit"),
]
