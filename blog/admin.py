# Register your models here.

from django.contrib import admin
from .models import Post   
# (.models指blog.models, Post为blog/models.py内的类)

# admin.site.register(Post)  
# 在admin页面注册，使显示。（创建了表不一定显示，主要在页面注册才显示）

@admin.register(Post)
# 作用同上，写法不同。 @ 符号为装饰器

class PostAdmin(admin.ModelAdmin):  # 配置展示格式和配置
    """
        :param: ClusterAdmin
        :return:
    """
    list_display = ('id','author','title','created_date','published_date')
    list_per_page = 10
    list_filter = ('author','id','title')  # id筛选
    search_fields = ('title','id') # 搜索筛选  ,支持模糊匹配搜索
    ordering = ('created_date',)  # 排序

class MyAdminSite(admin.AdminSite):   # 设置首页标签标题
    site_header = '后台配置'
    site_title = '后台配置'

admin_site = MyAdminSite(name = 'management')
