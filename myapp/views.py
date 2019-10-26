from django.shortcuts import render
from myapp.models import Category,Article,Banner,Tag,Link
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# Create your views here.
def global_variable(request):
    alltag1 = Tag.objects.all()[:10]  # 标签
    alltag2 = Tag.objects.all()[10:]
    allcat = Category.objects.all()  # 分类
    recommend = Article.objects.filter(recommend_id=1)[:4]
    return locals()


def index(request):
    # 右侧栏
    heatarticle1 = Article.objects.all().order_by('-views')[0:5]    # 热门排行
    heatarticle2 = Article.objects.all().order_by('-views')[5:10]    # 热门排行

    # 主体
    recommend = Article.objects.filter(recommend_id=1)[:3]  # 热门推荐位
    link = Link.objects.all()
    allbanner = Banner.objects.filter(is_active=True)[0:4]  # 轮播图图片
    allarticle = Article.objects.all().order_by('-id')[0:10]   # 文章列表
    return render(request, 'index.html',locals())


# 分类
def list(request,lid):
    list = Article.objects.filter(category_id=lid)  # 筛选对应文章
    cname = Category.objects.get(id=lid)  # 获取文章栏目名
    page = request.GET.get('page')  # 在URL中获取当前页面
    paginator = Paginator(list,4)  # 对查询到的数据对象list分页，设置4个对象为一页
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入不是整数是，只显示第1页
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入不在系统的页码列表中时，显示最后一页
    return render(request,'list.html',locals())


# 内容页
def show(request,sid):
    show = Article.objects.get(id=sid)  # 查询指定ID的文章
    hot = Article.objects.all().order_by('?')[:10]  # 内容下面的您可能感兴趣的文章，随机推荐
    previous_blog = Article.objects.filter(created_time__gt=show.created_time, category=show.category.id).first()
    netx_blog = Article.objects.filter(created_time__lt=show.created_time, category=show.category.id).last()
    show.views = show.views + 1
    show.save()
    return render(request,'show.html',locals())


# 标签页
def tag(request, tag):
    list = Article.objects.filter(tags__name=tag)  # 通过标签进行查询文章
    tname = Tag.objects.get(name=tag)  # 获取标签名
    page = request.GET.get('page')  # 在URL中获取当前页面
    pag = Paginator(list, 5)  # 对查询到的数据对象list分页，设置5个对象为一页
    try:
        list = pag.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = pag.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = pag.page(pag.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'tags.html', locals())


# 搜索页
def search(request):
    ss = request.GET.get('search')  # 获取搜索的关键词
    # list = Article.objects.filter(title__icontains=ss)   # 通过标签进行查询文章
    list = Article.objects.filter(Q(title__icontains=ss) | Q(body__icontains=ss))   # Q查询
    page = request.GET.get('page')  # 在URL中获取当前页面
    pag = Paginator(list, 4)  # 对查询到的数据对象list分页，设置5个对象为一页
    try:
        list = pag.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = pag.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = pag.page(pag.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request,'search.html',locals())


# 关于我们
def about(request):
    allcat = Category.objects.all()
    return render(request, 'page.html',locals())

