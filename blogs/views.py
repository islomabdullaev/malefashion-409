from django.shortcuts import render

from blogs.models import PostModel

# Create your views here.

def blog_details(request, pk):
    post = PostModel.objects.get(pk=pk)
    context = {
        "post": post
    }
    return render(request, template_name='blog-details.html', context=context)