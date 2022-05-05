from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from post.models import Post
from post.forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    context = {
        'title': 'Post list',
        'object_list': posts
    }
    return render(request, 'post/post_list.html', context)


def post_create(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Post created!!!")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'title': 'Post create',
        'form': form
    }
    return render(request, 'post/post_create.html', context)


def post_update(request, id):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href = '#'>Post created!!!</a> ", extra_tags='safe_html')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'title': 'Post update',
        'form': form
    }
    return render(request, 'post/post_create.html', context)


def post_delete(request, id):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    return redirect('post:post_list')


def post_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context = {
        'title': 'Post detail',
        'object': instance
    }
    return render(request, 'post/post_detail.html', context)
