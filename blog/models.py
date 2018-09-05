from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

# 分类
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 标签
class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 文章
class Post(models.Model):
    title = models.CharField(max_length=70)
    # 输入内容
    body = models.TextField()
    # 创建时间和修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    # blank=True，允许空值
    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category)
    # 标签允许空值就设定为blank=True
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User)

    class Meta:
        verbose_name = '文章信息'
        verbose_name_plural = verbose_name

    #如果不加这个方法，那么使用objects.all()方法调用返回的结果将是objects,
    #使用这个方法就可以调出实际的内容
    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})