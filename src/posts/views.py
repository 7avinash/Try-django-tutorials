from django.shortcuts import render, get_object_or_404, redirect
from models import *
from forms import *
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def post_list(request):
    object_list = Post.objects.all().order_by("-timestamp")

    paginator = Paginator(object_list, 25) # Show 25 object per page
    page = request.GET.get('page')

    try:
        object = paginator.page(page)
    except PageNotAnInteger:    # If page is not an integer, deliver first page.
        object = paginator.page(1)
    except EmptyPage:   # If page is out of range (e.g. 9999), deliver last page of results.
        object = paginator.page(paginator.num_pages)

    context = {"object":object}
    return render(request, 'index.html', context)

def post_detail(request,slug=None):
    instance = get_object_or_404(Post, slug=slug)
    context = {'object': instance}
    return render(request, 'detail.html', context)

def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "You have Successfully Created a Post")
            return redirect('posts:home')
        else:
            messages.error(request, "The post was not Created, Please Try Again")

    context = {"form":form}
    return render(request, 'create.html', context)

def post_update(request,slug=None):
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance= instance)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, "You have Successfully Updated a Post")
            return redirect('posts:home')
        else:
            messages.error(request, "The post was not Updated, Please Try Again")
    context = {"instance": instance, "form":form}
    return render(request, 'create.html', context)

def post_delete(request,slug=None):
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "You have Successfully Deleted a Post")
    return redirect('posts:home')

