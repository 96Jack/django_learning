from django.db import models


# Create your models here.

class User(models.Model):
    # flask 中必须写id  字符的类型必须指定长度
    # django 模型的属性必须制定长度  自动生成主键列
    name = models.CharField(max_length=32)  # 字符串的长度必须是2的倍数。
    age = models.IntegerField()
