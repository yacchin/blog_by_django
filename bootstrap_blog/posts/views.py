from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator
from bootstrap_blog.models import *


def index(request):
    get_page = request.GET.get(
        "page", False) if request.GET.get("page", False) else 1

    MAX_PAGE_NUM = 3

    class_ary = ["panel panel-primary",
                 "panel panel-success", "panel panel-warning"]

    posts = Post.objects.all()
    paginator = Paginator(posts, MAX_PAGE_NUM)
    page = paginator.page(get_page)

    tags = Tag.objects.all()
    users = User.objects.all()
    return render_to_response(
        'posts/index.html',
        {
            'page': page,
            'paginator': paginator,
            'class_ary': class_ary,
            'tags': tags,
            'users': users,
            'get_page': get_page,
        },
        context_instance=RequestContext(request)
    )


def show(request, post_id):
    posts = Post.objects.select_related().get(pk=post_id)
    return render_to_response(
        'posts/show.html',
        {
            'posts': posts,
            'labels': labels
        },
        context_instance=RequestContext(request)
    )


def new(request):
    return render_to_response(
        'posts/new.html',
        {


        },
        context_instance=RequestContext(request)
    )


def edit(request):
    return render_to_response(
        'posts/edit.html',
        {


        },
        context_instance=RequestContext(request)
    )
