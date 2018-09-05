from django.conf.urls import url

from . import views

# 通过使用视图函数命名空间来区分url中的name
app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # 从URL中把括号内匹配的字符串捕获并作为关键字参数传给对应的视图函数
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]