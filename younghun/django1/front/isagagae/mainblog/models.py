from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Test(models.Model):
    id = models.IntegerField(db_column='ID', primary_key = True)
    # 컬럼명이 id여서 기본키로 인식했음 -> 옵션을 primary_key = True로 줌
    local_code = models.IntegerField(db_column='LOCAL_CODE', blank=True, null=True)
    date_code = models.IntegerField(db_column='DATE_CODE', blank=True, null=True)
    price = models.IntegerField(db_column='PRICE', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'

class Memo(models.Model) :
    content = models.CharField(max_length=255)


class Star(models.Model) :
    id = models.IntegerField(primary_key=True)
    star_rate = models.IntegerField(db_column='rate', blank=True, null=True)

# class PetShopSurvey(models.Model):
#     i_like_snakes = LikertField()

