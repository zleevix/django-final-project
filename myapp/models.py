from typing import Tuple
from django import db
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class People(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        db_table = "People" # tên table tạo ra
        # Không còn tạo theo cái format <tên app viết thường>_<tên class model viết thường>

class Python2104(models.Model):

    ten = models.CharField(max_length=50) # CharFields có giới hạn về độ dài 
    tuoi = models.IntegerField()
    diachi = models.TextField()

    class Meta:
        db_table = "Python2104"

    

# Command:
# NOTE: Cần phải kiễm tra tên app đã được add vào INSTALL_APPS trong setting.py của project
# python manage.py makemigrations <tên app>: Kiểm tra sự thay đổi trên model tạo 1 file migrations
# python manage.py sqlmigrate <tên app> <number migrations>: Xem dưới dạng SQL command
# python manage.py migrate: Apply thay đổi xuống database

# Tạo mới 1 table có tên là <tên app viết thường>_<tên class model viết thường>


class Restaurant(models.Model):
    place = models.OneToOneField(
        "Place",
        on_delete=models.CASCADE,
       primary_key =True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name

    class Meta:
        db_table = "Restaurant"

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place" % self.name

    class Meta:
        db_table = "Place"

class Reporter(models.Model):
    first_name = models.CharField("Tên", max_length=30)
    last_name = models.CharField("Họ", max_length=30)
    email = models.EmailField("Địa chỉ email")
    # address = models.TextField("Địa chỉ", default="Hồ Chí")

    # def __str__(self):
    #     return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        db_table = "Reporter"

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['headline']
        db_table = "Article"

class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']
        db_table = "Publication"

    def __str__(self):
        return self.title

class BaiBao(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']
        db_table = "BaiBao"

    def __str__(self):
        return self.headline

# Upload file ảnh/video/audio lên server
class UserAvarta(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    avarta = models.ImageField(upload_to = "avarta")

    class Meta:
        db_table = "UserAvarta"