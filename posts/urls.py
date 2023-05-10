from django.urls import path
from posts.views import *

urlpatterns = [
    path("", create_post_list, name="create_post_list"),
    path("all/", get_post_list_all, name="get_post_list_all"),
    path("<int:id>", post_list_detail, name="post_list_detail"),
]
