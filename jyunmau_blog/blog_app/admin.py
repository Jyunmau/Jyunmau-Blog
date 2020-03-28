from django.contrib import admin
from blog_app.models import BlogsPost


# Register your models here.
class BlogsPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'brief', 'body', 'timestamp']


admin.site.register(BlogsPost, BlogsPostAdmin)
