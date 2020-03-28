from django.shortcuts import render
from blog_app.models import BlogsPost
import markdown


# Create your views here.
def blog_index(request):
    blog_list = BlogsPost.objects.order_by('-timestamp')[:3]
    return render(request, 'index.html', {'blog_list': blog_list})  # 返回index.html页面


def article_list(request):
    blog_list = BlogsPost.objects.all()  # 获取所有数据
    return render(request, 'article_list.html', {'blog_list': blog_list})


def article(request, article_id):
    blog = BlogsPost.objects.get(id=article_id)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'toc'
    ])
    content = md.convert(blog.body)
    return render(request, 'article.html', {'blog': blog, 'content': content, 'toc': md.toc})
