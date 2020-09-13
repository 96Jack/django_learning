from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from four.models import Four


def mysql(request):
    return HttpResponse('index')


# 增改需要save, 删查不需要save
def add_user(request):
    user = Four()
    user.name = "xzw"
    user.age = "23"

    # django 中只有save,flask中要commit,
    user.save()

    return HttpResponse('添加成功')


def find_id(request):
    # user = Four.objects.get(pk=1)
    users = Four.objects.all()
    for user in users:
        print(user.name, user.age)
    return HttpResponse("find ok")


def update(request):
    user = Four.objects.get(pk=2)
    user.name = 'qwe'
    user.save()

    return HttpResponse('update ok')


def delete(request):
    user = Four.objects.get(pk=3)
    print(user.name, user.age)
    user.delete()
    return HttpResponse('delete ok')
