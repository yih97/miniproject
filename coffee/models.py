from django.db import models

# Create your models here.
class Coffee(models.Model):
    brand = models.CharField(max_length=10)     # 브랜드
    coffee = models.CharField(max_length=20)    # 커피 종류
    coffee_name = models.CharField(max_length=20)
    price = models.IntegerField     # 가격
    caffeine = models.IntegerField      # 카페인
    sugar = models.IntegerField     # 당
    kcal = models.IntegerField       # 칼로리
