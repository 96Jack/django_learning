from django.http import HttpResponse
from two.models import Person
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('ok')


def testFilter(request):
    # persons = Person.objects.filter(age = 16)
    # for person in persons:
    #     print(person.name)
    # persons = Person.objects.exclude(age__gt=16)
    # for person in persons:
    #     print(person.name)

    # in  元组列表都可以
    # persons = Person.objects.filter(age__in=(17, 18))
    # for person in persons:
    #     print(person.name)

    # 链式调用
    persons = Person.objects.filter(age__gt=15).exclude(age=18)
    for person in persons:
        print(person.name, person.age)

    return HttpResponse("查询成功")
