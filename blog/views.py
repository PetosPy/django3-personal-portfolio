from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog

# Create your views here.
def all_blogs(request):
    blog_data = Blog.objects.order_by('-added_on')

    return render(request, 'blog/all_blogs.html', {"blog_data": blog_data})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    return render(request, "blog/details.html", {"blog": blog})