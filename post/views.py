from multiprocessing import context
from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from .models import Post
from comments.models import Comments

# Create your views here.
def index(request):
    allpost = Post.objects.all()
    context = {
        'allpost': allpost,
    }
    return render(request, 'post/index.html', context)

def details(request):
    postid = request.GET['id']
    post = Post.objects.filter(id=postid) #select * from Post where id = postid
    allcomment = Comments.objects.filter(post_id=postid).order_by('id').reverse()
    context= {
        'post':post,
        'allcomment':allcomment,
    }
    return render(request, 'post/details.html', context)



 