from django import forms
from django.core.validators import RegexValidator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# class PostForm(forms.Form):
#    title = forms.CharField()
#    content = forms.CharField()
#    phone = forms.CharField(
#        validators=[
#            RegexValidator(r"^\d{3}-?\d{4}-?\d{4}$", message="휴대폰 번호를 입력해주세요."),
#        ]
#    )
from diary.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = "__all__"
        # 유저로부터 입력받을 필드 이름을 나열
        # 이 필드에 대해서만, html, 유효성 검사, db 저장을 함
        fields = [
            "author_name",
            "title",
            "content",
            "photo",
            "tag_set",
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["author_name", "message"]


def post_new(request: HttpRequest) -> HttpResponse:
    form = PostForm
    return render(request, "diary/post_form.html", {
        "form": form,
    })
