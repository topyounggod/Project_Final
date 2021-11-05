from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=255)
    # user_pw = models.CharField(max_length=255, blank=True, null=True)
    # email = models.CharField(max_length=255, blank=True, null=True)
    # type_id = models.IntegerField(blank=True, null=True)
    hospital_rate = models.IntegerField(blank=True, null=True)
    pharmacy_rate = models.IntegerField(blank=True, null=True)
    playground_rate = models.IntegerField(blank=True, null=True)
    park_rate = models.IntegerField(blank=True, null=True)
    restaurant_rate = models.IntegerField(blank=True, null=True)
    cafe_rate = models.IntegerField(blank=True, null=True)
    salon_rate = models.IntegerField(blank=True, null=True)
    deliver_rate = models.IntegerField(blank=True, null=True)
    equip_rate = models.IntegerField(blank=True, null=True)
    sell_rate = models.IntegerField(blank=True, null=True)
    feed_rate = models.IntegerField(blank=True, null=True)
    manage_rate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'

class InfraType(models.Model):
    id = models.IntegerField(primary_key = True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infra_type'



# class Star(models.Model) :
#     id = models.IntegerField(primary_key=True)
#     star_rate = models.IntegerField(db_column='rate', blank=True, null=True)
#
# class StarRate(models.Model):
#     id = models.IntegerField(primary_key=True)
#     rate = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'star_rate'

class UserWeight(models.Model):
    user_weight_id = models.CharField(primary_key=True, max_length=255)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    subtype = models.CharField(max_length=255, blank=True, null=True)
    weight_rate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_weight'


# select box

