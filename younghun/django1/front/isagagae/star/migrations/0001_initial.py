# Generated by Django 3.2.9 on 2021-11-04 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('user_pw', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('type_id', models.IntegerField(blank=True, null=True)),
                ('hospital_rate', models.IntegerField(blank=True, null=True)),
                ('pharmacy_rate', models.IntegerField(blank=True, null=True)),
                ('playground_rate', models.IntegerField(blank=True, null=True)),
                ('park_rate', models.IntegerField(blank=True, null=True)),
                ('restaurant_rate', models.IntegerField(blank=True, null=True)),
                ('cafe_rate', models.IntegerField(blank=True, null=True)),
                ('salon_rate', models.IntegerField(blank=True, null=True)),
                ('deliver_rate', models.IntegerField(blank=True, null=True)),
                ('equip_rate', models.IntegerField(blank=True, null=True)),
                ('sell_rate', models.IntegerField(blank=True, null=True)),
                ('feed_rate', models.IntegerField(blank=True, null=True)),
                ('manage_rate', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserWeight',
            fields=[
                ('user_weight_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('user_id', models.CharField(blank=True, max_length=255, null=True)),
                ('subtype', models.CharField(blank=True, max_length=255, null=True)),
                ('weight_rate', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user_weight',
                'managed': False,
            },
        ),
    ]
