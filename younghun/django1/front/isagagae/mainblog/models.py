from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20)
    user_email = models.EmailField(unique=True)
    user_password = models.CharField(max_length=100)
    user_validate = models.BooleanField(default=False)

class Memo(models.Model) :
    content = models.CharField(max_length=255)


class Star(models.Model) :
    id = models.IntegerField(primary_key=True)
    star_rate = models.IntegerField(db_column='rate', blank=True, null=True)
#
# class UserID(models.Model):
#     user_id = models.CharField(max_length=20)
#     class Meta:
#         managed = False
#         db_table = 'user'
# class PetShopSurvey(models.Model):
#     i_like_snakes = LikertField()

