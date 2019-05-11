from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic. base import TemplateView
from django.utils import timezone
from .forms import BlogForm
from .models import Blog
# Create your views here.


class MainpageView(TemplateView):
    template_name = 'theme/main.html'


def blog(request):
    blogs = Blog.objects
    return render(request, 'theme/blog.html', {'blogs': blogs})


def contact(request):
    return render(request, 'theme/contact.html')


def home(request):
    return render(request, 'theme/home.html')


def blogform(request, blog=None):
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.pub_date = timezone.now()
            blog.save()
            return redirect('blog')
    else:
        form = BlogForm(instance=blog)
        return render(request, 'theme/contact.html', {'form': form})


def edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return blogform(request, blog)


def remove(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('blog')
