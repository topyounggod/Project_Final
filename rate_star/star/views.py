from MySQLdb.cursors import DictCursor
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import *
import random
import pymysql

# Create your views here.
def index(request) :
    if request.method == 'POST':
        hospital_rate = request.POST['rating1']
        pharmacy_rate = request.POST['rating1']
        playground_rate = request.POST['rating2']
        park_rate = request.POST['rating2']
        restaurant_rate = request.POST['rating3']
        cafe_rate = request.POST['rating3']
        salon_rate = request.POST['rating4']
        deliver_rate = request.POST['rating4']
        equip_rate = request.POST['rating5']
        sell_rate = request.POST['rating5']
        feed_rate = request.POST['rating5']
        manage_rate = request.POST['rating6']

        user = User()
        user.user_id = '테스트유저2'
        user.user_pw = '유저패스워드'
        user.email = 'melong@naver.com'
        user.type_id = '1'
        user.hospital_rate = hospital_rate
        user.pharmacy_rate = pharmacy_rate
        user.playground_rate = playground_rate
        user.park_rate = park_rate
        user.restaurant_rate = restaurant_rate
        user.cafe_rate = cafe_rate
        user.salon_rate = salon_rate
        user.deliver_rate = deliver_rate
        user.equip_rate = equip_rate
        user.sell_rate = sell_rate
        user.feed_rate = feed_rate
        user.manage_rate = manage_rate
        user.save()

        weight_rate = request.POST['rating7']
        subtype = request.POST['인프라 종류']

        user_weight = UserWeight()
        user_weight.user_weight_id = '1'
        user_weight.user_id = '테스트유저2'
        user_weight.subtype = subtype
        user_weight.weight_rate = weight_rate

        user_weight.save()

    return render(request, 'star/index.html')

def to_db(request):
    user_rate = pymysql.connect(
        user='root',
        passwd='1234',
        host='127.0.0.1',
        db='isagagae',
        charset='utf8',
        port = 3305
    )
    # print(request.GET)
    cursor = user_rate.cursor(pymysql.cursors.DictCursor)
    # insert_data=[{'rate': request.GET['checked']}]
    # insert_data=[{'rate': request.GET['checked']}]
    insert_data=[{'user_id': '테스트유저1','user_pw': '유저패스워드',
                  'email': '유저이메일', 'type_id': '3', 'rate': request.GET['checked']}]
    insert_sql = "INSERT INTO `user` VALUES (%(user_id)s,%(user_pw)s,%(email)s,%(type_id)s, %(rate)s);"
    print(insert_sql)
    cursor.executemany(insert_sql, insert_data)
    user_rate.commit()


def savestar(request) :
    print(request.GET['checked'])
    rate = request.GET['checked']
    # user_rate_id = random.randint(1, 100000)
    # user_id = random.randint(1, 100000)
    # type_id = random.randint(1, 100000)
    # rate = request.GET['checked']
    # data = {'user_rate_id' : user_rate_id,
    #         'user_id' : user_id,
    #         'type_id' : type_id,
    #         'rate' : rate}

    to_db(request)
    print('완료한 별점', rate)
    return redirect(reverse(index))

