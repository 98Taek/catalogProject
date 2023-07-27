from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from blog.forms import EmailPostForm, CommentForm
from blog.models import Post, Comment


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
    form = CommentForm()
    return render(request, 'blog/post/post_detail.html', {'post': post, 'form': form})


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{data['name']} 님이 {post.title}을(를) 추천합니다."
            message = f"{post.title} 을(를) {post_url}에서 읽어보세요.\n\n" \
                      f"{data['name']}의 의견: {data['message']}"
            send_mail(subject, message, '98taek@gamil.com', [data['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/post_share.html', {'post': post, 'form': form, 'sent': sent})


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect(post)
    return render(request, 'blog/post/post_detail.html', {'post': post, 'form': form})
