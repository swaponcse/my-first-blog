from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone

from django.shortcuts import render, get_object_or_404
from .models import Post, Comment,student

from django.shortcuts import redirect
from .forms import studentForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_list2(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/others.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def publish(self):
    self.published_date = timezone.now()
    self.save()

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)




def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

def base(request):
    return render(request,'blog/base.html')

def gallery(request):
    return render(request,'blog/gallery.html')
def contact(request):
    return render(request,'blog/contact.html')
def services(request):
    return render(request,'blog/services.html')

def deptresource(request):
    return render(request,'blog/deptresource.html')

def nondeptresource(request):
    return render(request,'blog/nondeptresource.html')

def dept(request):
    return render(request,'blog/dept.html')

def nondept(request):
    return render(request,'blog/nondept.html')

def reg(request):
    return render(request,'blog/reg.html')

def blogs(request):
    return render(request,'blog/blogs.html')

def contacts(request):
    return render(request,'blog/contacts.html')


def studentlist(request):
    studentlists = student.objects.all();
    return render(request, 'blog/reg.html', {'studentlists': studentlists})




def regshow(request):
    if request.method == "POST":
        form = studentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('rspshow')
    else:
        form = studentForm()
        return render(request, 'blog/regshow.html', {'form': form})

def rspshow(request):
    students= student.objects.filter(name__lte=all).order_by('id')
    return render(request, 'blog/rsp.html', {'students': students})