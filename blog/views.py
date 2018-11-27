from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Article, Category, Banner, Tag, Link
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

def global_variable(request):
    allcategory = Category.objects.all()
    remen = Article.objects.filter(tui_id=2)[:6]
    tags = Tag.objects.all()
    return locals()

def index(request):
    banner = Banner.objects.filter(is_active=True)[0:4]
    tui = Article.objects.filter(tui_id=1)[:3]
    allarticle = Article.objects.all().order_by('-id')[0:10]
    hot = Article.objects.all().order_by('views')[:10]
    links =  Link.objects.all()
    return render(request, 'index.html',locals())


def list(request,lid):
    list = Article.objects.filter(category_id=lid)
    cname = Category.objects.get(id=lid)
    page = request.GET.get('page')
    paginator = Paginator(list,5)
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return render(request, 'list.html', locals())


def show(request,sid):
    show = Article.objects.get(id=sid)
    hot = Article.objects.all().order_by('?')[:10]
    previous_blog = Article.objects.filter(created_time__gt=show.created_time,category=show.category.id).first()
    next_blog = Article.objects.filter(created_time__lt=show.created_time,category=show.category.id).last()
    show.views = show.views + 1
    show.save()
    return render(request,'show.html', locals())


def tag(request,tag):
    list = Article.objects.filter(tags__name=tag)  # 通过文章标签进行查询文章
    tname = Tag.objects.get(name=tag)  # 获取当前搜索的标签名
    page = request.GET.get('page')
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'tags.html', locals())

def search(request):
    ss = request.GET.get('search')
    list = Article.objects.filter(title__icontains=ss)
    page = request.GET.get('page')
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'search.html', locals())


def about(request):
    allcategory = Category.objects.all()
    return render(request, 'page.html',locals())