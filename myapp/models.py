from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField


class Category(models.Model):
    name = models.CharField(verbose_name='分类名',max_length=100)
    index = models.IntegerField ( default=99, verbose_name='分类排序' )

    class Mete:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    id = models.AutoField(verbose_name='序号',max_length=11,primary_key=True)
    name = models.CharField(verbose_name='标签名',max_length=30)

    class Mete:
        verbose_name = '文章标签'

    def __str__(self):
        return self.name

class Recommend(models.Model):
    name = models.CharField(verbose_name='推荐位',max_length=30)

    class Mete:
        verbose_name = '推荐位'

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(verbose_name='文章标题',max_length=100)
    excerpt = models.TextField('摘要',max_length=200,blank=True)
    category = models.ForeignKey(Category,verbose_name='分类表',blank=True,null=True,on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag,verbose_name='标签表',blank=True)
    img = models.ImageField(upload_to='artice_img/%Y/%m/%d/',verbose_name='文章图片',blank=True,null=True)
    body = UEditorField('编辑内容',width=800,height=500,toolbars="full",imagePath='upimg/',filePath='upfile/',upload_settings={'imageMaxSize':1204000},settings={},command=None,blank=True)
    user = models.ForeignKey(User,verbose_name='作者',blank=True,on_delete=models.CASCADE)
    views = models.PositiveIntegerField('阅读量',default=0)
    recommend = models.ForeignKey(Recommend,verbose_name='推荐位表',blank=True,on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField('发布时间',auto_now_add=True)
    modified_time = models.DateTimeField('修改时间',auto_now=True)

    class Mete:
        verbose_name = '文章'

    def __str__(self):
        return self.title


class Banner(models.Model):
    text_info = models.CharField(verbose_name='图片标题',max_length=100,default='')
    img = models.ImageField('轮播图',upload_to='banner/')
    link_url = models.URLField('图片链接',max_length=100)
    is_active = models.BooleanField('是否是active',default=False)
    name = models.CharField(verbose_name='图片名称',max_length=100,null=True)

    class Mete:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'

    def __str__(self):
        return self.text_info

class Link(models.Model):
    name = models.CharField(verbose_name='友情链接名',max_length=70)
    linkurl = models.URLField()

    class Mete:
        verbose_name = '友情链接'

    def __str__(self):
        return self.name