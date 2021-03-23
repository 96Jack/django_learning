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
    url(r'add_grade/', views.add_grade),
    # url(r'add_student/', views.add_student),

    # 一对多查询
    # 给定主表数据查询从表数据
    # 给定从表数据查询主表数据
    # 模型属性的名字使用小驼峰  :  userName
    # 模型字段的名字使用下划线  :  user_name

    url(r'^getDname/', views.getDname),
    url(r'^getEname/', views.getEname),

]