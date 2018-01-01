from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    re_path('example/$', views.example,name="calc_example"),
    re_path('index/$', views.cal_index,name="calc_index"),
    re_path('^$', views.cal_index,name="calc_index"),
    re_path('add/$', views.add_with_params, name="calc_add_with_params"),
    re_path('add/([\d]+)/([\d]+)/$', views.add, name="calc_add"),
]
