from django.db import models


# Create your models here.
class Goods(models.Model):
    name = models.CharField(max_length=32)
    length = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    way = models.CharField(max_length=32)
    locate = models.CharField(max_length=32)
    package = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    weight = models.IntegerField(default=0)
    num = models.IntegerField(default=0)

    class Meta:
        db_table = "goods"

class Users(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

    class Meta:
        db_table = "blog_users"