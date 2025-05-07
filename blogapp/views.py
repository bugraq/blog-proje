from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm  # Yeni post eklemek için bir form sınıfı

def home(request):
    posts = Post.objects.all().order_by('-created_at')  # En yeni gönderiler önce
    return render(request, 'blogapp/home.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blogapp/post_detail.html', {'post': post})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # post eklendikten sonra ana sayfaya git
    else:
        form = PostForm()
    return render(request, 'blogapp/add_post.html', {'form': form})
