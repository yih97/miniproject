from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Community(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Communities"



class Coffee(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    brand = models.CharField(max_length=10)     # 브랜드
    coffee = models.CharField(max_length=20)    # 커피 종류
    coffee_name = models.CharField(max_length=20)
    price = models.IntegerField()     # 가격
    caffeine = models.IntegerField(null=True)      # 카페인
    sugar = models.IntegerField(null=True)     # 당
    kcal = models.IntegerField(null=True)       # 칼로리


        



