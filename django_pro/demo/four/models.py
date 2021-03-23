from django.db import models

# Create your models here.
from django.db import models


class Four(models.Model):
    # flask 中必须写id  字符的类型必须指定长度
    # django 模型的属性必须制定长度  自动生成主键列
    name = models.CharField(max_length=32)  # 模型的字段的长度必须是2的倍数。
    age = models.IntegerField()


class Grade(models.Model):
    name = models.CharField(max_length=32)  # 字段


class Student(models.Model):
    name = models.CharField(max_length=32)
    s_grade = models.ForeignKey(Grade,on_delete=models.CASCADE)


# 主表
class Dept(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        db_table = 'Dept'


# 从表
class Emp(models.Model):
    name = models.CharField(max_length=32)
    #  从表外键设置
    e_dept = models.ForeignKey(Dept,on_delete=models.CASCADE)

    class Meta:
        db_table = 'Emp'


class Bird(models.Model):
    name = models.CharField(max_length=32)
    color = models.CharField(max_length=32)

    class Meta:
        db_table = 'bird'


