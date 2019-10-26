from django.contrib import admin
from .models import Banner,Category,Tag,Recommend,Article,Link
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'category',
                    'title',
                    'recommend',
                    'user',
                    'views',
                    'created_time'
                    )
    list_per_page = 50
    ordering = ('-created_time',)
    list_display_links = ('id','title')

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'text_info',
                    'img',
                    'link_url',
                    'is_active'
                    )
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name'
                    )
@admin.register(Recommend)
class RecommendAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name'
                    )
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name'
                    )
@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'linkurl'
                    )