from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Post
from .forms import PostForm

# Post list view.
def home(request):
    posts = Post.objects.all().order_by('-date_published')
    return render(request, 'blog/index.html', {'posts':posts})

# Create post.
def add_post(request):
    if request.method=='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your new post has been added!")
            return redirect('blog-list-view')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form':form})

# Post detail view.
def read_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'blog/read_post.html', {'post':post})

# View for post search
def search_post(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        posts = Post.objects.filter(title__contains=search_query)
        return render(request, 'blog/search_post.html', {'query':search_query, 'posts':posts})
    else:
        return render(request, 'blog/search_post.html',{})