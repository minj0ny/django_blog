from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic. base import TemplateView
from django.utils import timezone
from .forms import BlogForm, CommentForm, HashtagForm
from .models import Blog, Comment, Hashtag
# Create your views here.


class MainpageView(TemplateView):
    template_name = 'theme/main.html'


def blog(request):
    blogs = Blog.objects
    hashtags = Hashtag.objects
    return render(request, 'theme/blog.html', {'blogs': blogs, 'hashtags': hashtags})


def contact(request):
    return render(request, 'theme/contact.html')


def home(request):
    return render(request, 'theme/home.html')


def blogform(request, blog=None):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES,instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.pub_date = timezone.now()
            blog.save()
            form.save_m2m()
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


def detail(request, pk, comment=None):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog_id = blog
            comment.comment_text = form.cleaned_data["comment_text"]
            comment.save()
            return redirect('detail', pk)
    else:
        form = CommentForm(instance=comment)
        return render(request, 'theme/detail.html', {"blog": blog, "form": form})


def comment_edit(request, pk, blog_pk):
    comment = get_object_or_404(Comment, pk=pk)
    return detail(request, blog_pk, comment)


def comment_remove(request, pk, blog_pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('detail', blog_pk)


def hashtagform(request, hashtag=None):
    if request.method == "POST":
        form = HashtagForm(request.POST, instance=hashtag)
        if form.is_valid():
            hashtag = form.save(commit=False)
            if Hashtag.objects.filter(name=form.cleaned_data['name']):
                form = HashtagForm()
                error_message = "이미 존재하는 해시태그 입니다."
                return render(request, 'theme/hashtag.html', {'form': form, 'error_message': error_message})
            else:
                hashtag.name = form.cleaned_data['name']
                hashtag.save()
                return redirect('home')
    else:
        form = HashtagForm(instance=hashtag)
        return render(request, 'theme/hashtag.html', {'form': form})


def search(request, hashtag_id):
    hashtag = get_object_or_404(Hashtag, pk=hashtag_id)
    return render(request, 'theme/search.html', {'hashtag': hashtag})
