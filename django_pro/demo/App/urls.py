from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'index/', views.index),
    url(r'rander/', views.testrander),
    url(r'^Tem_old/', views.Tem_old)
]
