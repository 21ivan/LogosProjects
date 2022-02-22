from django.shortcuts import render
from post.models import Post


# Create your views here.
def post_list(request):
    instance = Post.objects.all()
    context = {'Title': 'Post list',
               'objects': instance
               }
    return render(request, 'index.html', context)
