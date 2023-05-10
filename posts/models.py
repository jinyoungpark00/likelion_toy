from django.db import models


# Create your models here.
class Post_list(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="제목", max_length=20)
    author = models.CharField(verbose_name="작성자", max_length=10)
    content = models.CharField(verbose_name="내용", max_length=100)
