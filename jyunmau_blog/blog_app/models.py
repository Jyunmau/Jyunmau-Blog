from django.db import models


# Create your models here.
class BlogsPost(models.Model):
    title = models.CharField(max_length=150)  # 博客标题
    author = models.CharField(max_length=20)  # 博客标题
    category = models.CharField(max_length=150)  # 博客标题
    brief = models.TextField()  # 博客摘要
    body = models.TextField()  # 博客正文
    timestamp = models.DateTimeField()  # 创建时间
    id = models.AutoField(primary_key=True)
