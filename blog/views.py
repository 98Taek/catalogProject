from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from blog.models import Post


def post_list(request):
    post_list = Post.objects.filter(status=Post.Status.PUBLISHED).all()
    per_page = request.GET.get('per_page', 3)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(post_list, per_page, orphans=1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/post_list.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/post_detail.html', {'post': post})
