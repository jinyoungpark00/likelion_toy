from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Post_list
import json


# Create your views here.
@require_http_methods("[GET], [POST]")
def post_list(request):
    if request.method == "GET":
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
                "message": "읽어오기 성공",
                "data": posts_json,
            }
        )

    elif request.method == "POST":
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


@require_http_methods("[GET], [POST]")
def post(request, id):
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
