from django.shortcuts import render, HttpResponse, redirect 
from datetime import datetime
from django.contrib import messages
from blog.models import Post, BlogComment
from django.contrib.auth.models import User


def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request,'blog/blogHome.html',  context)

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    context={'post':post,'user': request.user}
    return render(request, "blog/blogPage.html", context)
    

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        comment=BlogComment(comment= comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")
        
    return redirect(f"/blog/{post.slug}")