from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from four.models import Four, Grade, Student, Emp, Dept


def mysql(request):
    return HttpResponse('index')


# 增改需要save, 删查不需要save
def add_user(request):
    user = Four()
    # user.name = "徐志文"
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


def add_grade(request):
    user = Grade()
    # user.name = "python"
    # user.name = "java"
    user.name = "c"
    # django 中只有save,flask中要commit,
    user.save()

    return HttpResponse('添加成功')


# def add_student(request):
#     student = Student()
#     grade = Grade()
#     # user.name = "哈哈"
#     # user.name = "徐志文"
#     student.name = "xzw"
#     student.s_grade = "1"
#     # user.s_grade = 2
#     # user.s_grade = 3
#
#     # django 中只有save,flask中要commit,
#     student.save()
#
#     return HttpResponse('添加成功')

#   一对多的查询
#    通过从表查询主表
def getDname(rquest):
    emp = Emp.objects.filter(name='迪丽热巴')[0]
    # 各大框架filter的数据返回类型
    # flask(BaseQuery)  tornado(Query)  django(QuerySet)
    print(emp.e_dept.name)
    return HttpResponse('查询成功')

#    通过主表查询从表
def getEname(request):
    dept = Dept.objects.filter(name='开发部门')[0]
    emps = dept.emp_set.all()
    for emp in emps:
        print(emp.name)
        print(emp.id)
    return HttpResponse('查询成功')
