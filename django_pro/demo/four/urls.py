from django.conf.urls import url
from four import views

urlpatterns = [
    url(r'mysql/', views.mysql),
    # 添加数据
    url(r'add_user/', views.add_user),
    # 查询 （删除建立在查询基础之上）
    url(r'find_id/', views.find_id),
    # 修改
    url(r'update/', views.update),
    # 删除
    url(r'delete/', views.delete),
]