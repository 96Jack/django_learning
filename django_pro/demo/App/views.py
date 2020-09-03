
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from django.template import loader


def index(request):
    return HttpResponse("this the sub_url for django")


def testrander(request):
    # render的返回值类型是HttpResponse ，第一个参数是request，第二个参数是页面
    context = {
        'name':'zs',
        'score_list':[100,82,90,56,77,88,122],
    }

    return render(request, 'score.html', context=context)

#模板的底层实现
def Tem_old(request):
    # 加载页面
    html_obj = loader.get_template('score_1.html')
    context = {
        'name' : 'zs',
    }
    # 渲染页面
    context_obj = html_obj.render(context=context)

    return HttpResponse(context_obj)