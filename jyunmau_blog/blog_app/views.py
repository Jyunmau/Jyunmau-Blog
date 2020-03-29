from django.shortcuts import render
from blog_app.models import BlogsPost
import markdown


# Create your views here.
def blog_index(request):
    blog_list = BlogsPost.objects.order_by('-timestamp')[:3]
    category_list = []
    categories = BlogsPost.objects.values('category')
    for cate in categories:
        if not (cate["category"] in category_list):
            category_list.append(cate["category"])
    return render(request, 'index.html', {'blog_list': blog_list, 'category_list': category_list})  # 返回index.html页面


def article_list(request):
    Big_Title = '全 部 文 章'
    Big_Brief = '也没多少篇嘛，慢慢来'
    blog_list = BlogsPost.objects.all()
    category_list = []
    categories = BlogsPost.objects.values('category')
    for cate in categories:
        if not (cate["category"] in category_list):
            category_list.append(cate["category"])
    return render(request, 'article_list.html', {'blog_list': blog_list,
                                                 'category_list': category_list,
                                                 'BigTitle': Big_Title,
                                                 'BigBrief': Big_Brief})


def article_list_cate(request, cat):
    Big_Title = '分 类 文 章 - '
    Big_Brief = '也没多少篇嘛，慢慢来'
    blog_list = BlogsPost.objects.filter(category=cat)
    category_list = []
    categories = BlogsPost.objects.values('category')
    for cate in categories:
        if not (cate["category"] in category_list):
            category_list.append(cate["category"])
    return render(request, 'article_list.html', {'blog_list': blog_list,
                                                 'category_list': category_list,
                                                 'BigTitle': Big_Title + cat,
                                                 'BigBrief': Big_Brief})


def article(request, article_id):
    blog = BlogsPost.objects.get(id=article_id)
    category_list = []
    categories = BlogsPost.objects.values('category')
    for cate in categories:
        if not (cate["category"] in category_list):
            category_list.append(cate["category"])
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'toc'
    ])
    content = md.convert(blog.body)
    return render(request, 'article.html',
                  {'blog': blog, 'content': content, 'toc': md.toc, 'category_list': category_list})
