from django.shortcuts import render
from blog.models import Post

# Create your views here.


def demo(request):
    # context = Post.objects.get(id=1)
    context = {"id":12345,"name":"我是第一篇博客"}
    return render(request, 'post_list.html', context)