from django.shortcuts import render, redirect
from .forms import PostItemForm
from .models import Post
# Create your views here.

def get_posts(request):
    return render(request, "blog/post_list.html")
    
def create_posts(request):
    if request.method=="POST":
        form = PostItemForm(request.POST)
        message = form.save(commit=False)
        message.author = request.user
        message.save()
        return redirect('inbox')
    else:
        form = PostItemForm()
    
    items = PostItemForm()
    return render(request, "blog/post_details.html", { 'form': form, 'items': items})