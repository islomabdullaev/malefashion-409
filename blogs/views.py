from django.http import HttpResponse
from django.shortcuts import redirect, render

from blogs.models import CommentModel, PostModel
from blogs.forms import CreateCommentForm

# Create your views here.

def blog_details(request, pk):
    post = PostModel.objects.get(pk=pk)
    form = CreateCommentForm()
    if request.method == "POST":
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            form.save()
            return redirect('blogs:details', pk=pk)

    context = {
        "post": post,
        "form": form
    }
    return render(request, template_name='blog-details.html', context=context)
