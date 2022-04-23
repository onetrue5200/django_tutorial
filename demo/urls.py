from django.urls import path, re_path, include
from . import views
# 注册自定义路径转化器
from django.urls import register_converter
from . import converters
register_converter(converters.CustomYearConverter, 'yyyy')

app_name = 'demo'

urlpatterns01 = [
    # ''' 常用路径转化器 '''
    # path('', views.url_standard_number),  # number默认值
    path('0/', views.url_standard_fix, name='url_standard_fix'),  # 固定路径
    # path('<int:number>/', views.url_standard_number),  # int型
    # path('<uuid:uuid>/', views.url_standard_uuid),  # uuid
    # path('<slug:slug>/', views.url_standard_slug),  # slug
    # path('<str:str>/', views.url_standard_str),  # str
    # path('<path:path>/', views.url_standard_path),  # path
    # ''' 自定义路径转化器 '''
    # re_path(r'^custom/re/(?P<year>[0-9]{4})/$', views.url_custom_year),
    # path('custom/<yyyy:year>/', views.url_custom_year),
    # redirect
    path('redirect/', views.redirect)
]

urlpatterns = [
    # path('url/', include(urlpatterns01)),
    # path('cbv/', views.Class_Base_View.as_view()),
    path('index/', views.index, name='index'),
]
