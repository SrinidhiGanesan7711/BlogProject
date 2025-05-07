from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def postList(request):
    query = request.GET.get("q")
    posts = BlogPost.objects.all().order_by('-created_at')
    if query:
        posts = posts.filter(Q(title__icontains=query))
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/pList.html', {'posts': posts})

def postDetail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/pDetail.html', {'post': post})

@login_required
def postCreate(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pList')
    else:
        form = BlogPostForm()
    return render(request, 'blog/pForm.html', {'form': form})

@login_required
def postEdit(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    form = BlogPostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('pList')
    return render(request, 'blog/pForm.html', {'form': form})

@login_required
def postDelete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('pList')
    return render(request, 'blog/pConfirmDelete.html', {'post': post})
