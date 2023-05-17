from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Post_list
import json


# Create your views here.


# 방명록 모두 가져오기
@require_http_methods("[GET]")
def get_post_list_all(request):
    posts = Post_list.objects.all()
    posts_json = []

    for post in posts:
        post_json = {
            "post_id": post.post_id,
            "author": post.author,
            "title": post.title,
            "content": post.content,
        }

        posts_json.append(post_json)

    return JsonResponse(
        {
            "status": 200,
            "massage": "방명록 모두 불러오기 성공",
            "data": posts_json,
        }
    )


# 방명록 추가
@require_http_methods("[POST]")
def create_post_list(request):
    body = json.loads(request.body.decode("utf-8"))

    new_post = Post_list.objects.create(
        author=body["author"],
        title=body["title"],
        content=body["content"],
    )

    new_post_json = {
        "id": new_post.post_id,
        "author": new_post.author,
        "title": new_post.title,
        "content": new_post.content,
    }

    return JsonResponse(
        {
            "status": 200,
            "message": "post 성공",
            "data": new_post_json,
        }
    )


# 방명록 가져오기, 삭제
@require_http_methods("[GET], [DELETE]")
def post_list_detail(request, id):
    if request.method == "GET":
        post = get_object_or_404(Post_list, pk=id)

        post_json = {
            "author": post.author,
            "title": post.title,
            "content": post.content,
        }

        return JsonResponse(
            {
                "status": 200,
                "message": "방명록 하나 읽어오기",
                "data": post_json,
            }
        )

    elif request.method == "DELETE":
        delete_post = get_object_or_404(Post_list, pk=id)
        delete_post.delete()

        return JsonResponse({"status": 200, "message": "게시글 삭제 성공", "data": None})
