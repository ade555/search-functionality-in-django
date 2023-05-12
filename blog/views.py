from django.shortcuts import render
from django.db.models import Q
from .models import Post

# Post list view.
def home(request):
    posts = Post.objects.all().order_by('-date_published')
    return render(request, 'blog/index.html', {'posts':posts})

# View for search feature
def search_post(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        posts = Post.objects.filter(title__contains=search_query)
        return render(request, 'blog/search_post.html', {'query':search_query, 'posts':posts})
    else:
        return render(request, 'blog/search_post.html',{})


"""
Uncomment below to search by more than one field.
"""
# def search_post(request):
#     if request.method == 'POST':
#         search_query = request.POST['search_query']
#         posts = Post.objects.filter(Q(title__icontains=search_query) | Q(title__icontains=search_query))
#         return render(request, 'blog/search_post.html', {'query':search_query, 'posts':posts})
#     else:
#         return render(request, 'blog/search_post.html',{})