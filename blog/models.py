from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone

# 数据库字段定义
# 类型（django定义的数据库类型方法）
# 1. models.ImageField(图片类型)   2. models.FildField（文件类型）
class Post(models.Model):
    # 作者  外键（ForeignKey） 若删除则连用户表的内容也一并删除（on_delete=models.CASCADE）
    # 外键不能作为筛选条件
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # 标题  字符串类型（CharField） 
    title = models.CharField(max_length=200)  
    # 文章内容
    text = models.TextField()  # 文本型
    # 收藏数量
    col_num = models.IntegerField()  # 整形
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):  # 发布 （实例方法）
        self.published_date = timezone.now()
        self.save()


    def __str__(self):  # __（两个下划线） 指python内置方法
        return self.title   # 返回文章标题