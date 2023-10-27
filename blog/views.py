from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from django.views.generic import ListView

from .forms import CommentForm
from .models import Category, Post, Tag, Comment


def post_view(request):
    posts = Post.objects.all()[:3]

    context = {
        "posts": posts,
    }
    return render(request, 'index.html', context=context)


# def blog(request):
#     posts = Post.objects.all()
#
#     paginator = Paginator(posts, per_page=1)
#     page_number = request.GET.get("page", '')
#     page_obj = paginator.get_page(page_number)
#
#     context = {
#         "posts": posts,
#         "page": page_obj,
#     }
#     return render(request, 'blog.html', context=context)

class PostView(ListView):
    queryset = Post.objects.all()
    template_name = 'blog.html'
    context_object_name = 'posts'
    paginate_by = 1


def detail(request, pk):
    post = get_object_or_404(Post, id=pk)

    comments = post.comments.filter(active=True)
    print(comments)

    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.post = post
        new_comment.save()

        return redirect(post.get_absolute_url()+'#'+str(new_comment.id))
    else:
        comment_form = CommentForm()

    context = {
        "post": post,
        'comments': comments,
    }

    return render(request, 'single.html', context=context)
