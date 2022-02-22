from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from post.models import Post
from post.forms import PostForm


def home_page(request):
    posts = Post.objects.all()
    context = {
        'title': 'Post list',
        'object_list': posts
    }
    return render(request, 'post/home_page.html', context)


def post_create(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
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
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'title': 'Post update',
        'form': form
    }
    return render(request, 'post/post_create.html', context)


def post_delete(request):
    return HttpResponse('<h1>post delete</h1>')


def post_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context = {
        'title': 'Post detail',
        'object': instance
    }
    return render(request, 'post/post_detail.html', context)
