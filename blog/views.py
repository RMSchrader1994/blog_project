from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostItemForm

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {'posts': posts})
    
    
def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, "blog/post_detail.html", {'post': post})
    
def delete_post(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect("post_list")
    
def create_posts(request):
    if request.method=="POST":
        form = PostItemForm(request.POST)
        message = form.save(commit=False)
        message.author = request.user
        message.save()
        return redirect('post_list')
    else:
        form = PostItemForm()
    
    items = PostItemForm()
    return render(request, "blog/create.html", { 'form': form, 'items': items})
    
def edit_post(request, id): 
    post = get_object_or_404(Post, pk=id)

    if request.method == "POST":
        print("It's the POST")
        form = PostItemForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_list")
    else:
        print("It's the GET")
        
    form = PostItemForm(instance=post)
    return render(request, "blog/create.html", {'form': form})