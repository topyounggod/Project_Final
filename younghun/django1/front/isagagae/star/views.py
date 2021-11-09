from MySQLdb.cursors import DictCursor
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import *
import pymysql
from pathlib import Path
import pandas as pd
from .findNearInfras import nearInfras

from django.contrib.auth.models import User
BASE_DIR = Path(__file__).resolve().parent.parent



# Create your views here.


def starindex(request) :
    return render(request, 'star/star_index.html')
    # user = User_table()
    # user.user_id = User.objects.get(username=request.user.get_username())

    # if request.method == 'POST':
    #     hospital_rate = request.POST['rating1']
    #     pharmacy_rate = request.POST['rating1']
    #     playground_rate = request.POST['rating2']
    #     park_rate = request.POST['rating2']
    #     restaurant_rate = request.POST['rating3']
    #     cafe_rate = request.POST['rating3']
    #     salon_rate = request.POST['rating4']
    #     deliver_rate = request.POST['rating4']
    #     equip_rate = request.POST['rating5']
    #     sell_rate = request.POST['rating5']
    #     feed_rate = request.POST['rating5']
    #     manage_rate = request.POST['rating6']
    #
    #     user = User_table()
    #     # userID = UserID()
    #     user.user_id = User.objects.get(username=request.user.get_username())
    #     # userID.save()
    #     # user.user_id = User.objects.get(username = request.user.get_username())
    #     # user.user_id =
    #     # user.user_pw = request.user.password
    #     # user.email = 'melong@naver.com'
    #     # user.type_id = '1'
    #     user.hospital_rate = hospital_rate
    #     user.pharmacy_rate = pharmacy_rate
    #     user.playground_rate = playground_rate
    #     user.park_rate = park_rate
    #     user.restaurant_rate = restaurant_rate
    #     user.cafe_rate = cafe_rate
    #     user.salon_rate = salon_rate
    #     user.deliver_rate = deliver_rate
    #     user.equip_rate = equip_rate
    #     user.sell_rate = sell_rate
    #     user.feed_rate = feed_rate
    #     user.manage_rate = manage_rate
    #     user.save()

        # weight_rate = request.POST['rating7']
        # subtype = request.POST['인프라 종류']
        #
        # user_weight = UserWeight()
        # user_weight.user_weight_id = '1'
        # user_weight.user_id = '테스트유저2'
        # user_weight.subtype = subtype
        # user_weight.weight_rate = weight_rate
        #
        # user_weight.save()

    # return render(request, 'star/star_index.html')


def showpinmap(request):
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

        user = User_table()
        # userID = UserID()
        user.user_id = User.objects.get(username=request.user.get_username())
        # userID.save()
        # user.user_id = User.objects.get(username = request.user.get_username())
        # user.user_id =
        # user.user_pw = request.user.password
        # user.email = 'melong@naver.com'
        # user.type_id = '1'
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
    db = pymysql.connect(
        user='root',
        password='1111',
        host='127.0.0.1',
        db='isagagae',
        charset='utf8',
        port=3307
    )

    cursor = db.cursor(pymysql.cursors.DictCursor)

    sql = "select lat_, lng_ " \
          "from(" \
          "select r.hospital * u.hospital_rate + r.pharmacy * u.pharmacy_rate + " \
          "r.play * u.playground_rate + r.park * u.park_rate + " \
          "r.restaurant * u.restaurant_rate + r.cafe * u.cafe_rate + " \
          "r.beauty * u.salon_rate + r.deliver * u.deliver_rate + " \
          "r.equip * u.equip_rate + r.sell * u.sell_rate + " \
          "r.food * u.feed_rate + r.manage * u.manage_rate as sum, " \
          "r.lat lat_, r.lng lng_, cluster " \
          "from cluster_result r, user u " \
          "where user_id = '"+ str(User.objects.get(username=request.user.get_username()))+ "' "\
          "order by sum desc " \
          "limit 30)" \
          "a;"

    cursor.execute(sql)

    result = cursor.fetchall()
    result = pd.DataFrame(result)

    # csvfile = BASE_DIR /'static/json/random_pinpoint.csv'
    # # sql => query문에서 나온 그 좌표 세 개로
    # pointdata = pd.read_csv(csvfile)
    print(result)
    latlng = []
    for lat, lng in zip(result['lat_'], result['lng_']):
        center = [lat, lng]
        nearpoints = nearInfras(center)
        redpoints = []
        for infra in nearpoints:
            if infra['type'] == 'Feature' :
                redpoints.append({
                    "infraname":infra['properties']['name'],
                    "infratype":infra['properties']['type'],
                    "infralat":infra['geometry']['coordinates'][1],
                    "infralng":infra['geometry']['coordinates'][0]
                })
            else:
                redpoints.append({
                    "infraname": infra['name'],
                    "infratype": infra['type'],
                    "infralat": infra['geometry']['coordinates'][1],
                    "infralng": infra['geometry']['coordinates'][0]
                })
        latlng.append({"lat":lat, "lng":lng, "near":redpoints})
    context = {
         'latlngs': latlng
    }
    return render(request, 'star/pinpointmap.html', context=context)

# def to_db(request):
#     user_rate = pymysql.connect(
#         user='root',
#         passwd='1234',
#         host='127.0.0.1',
#         db='isagagae',
#         charset='utf8',
#         port = 3305
#     )
#     # print(request.GET)
#     cursor = user_rate.cursor(pymysql.cursors.DictCursor)
#     # insert_data=[{'rate': request.GET['checked']}]
#     # insert_data=[{'rate': request.GET['checked']}]
#     insert_data=[{'user_id': '테스트유저1','user_pw': '유저패스워드',
#                   'email': '유저이메일', 'type_id': '3', 'rate': request.GET['checked']}]
#     insert_sql = "INSERT INTO `user` VALUES (%(user_id)s,%(user_pw)s,%(email)s,%(type_id)s, %(rate)s);"
#     print(insert_sql)
#     cursor.executemany(insert_sql, insert_data)
#     user_rate.commit()


# def savestar(request) :
#     print(request.GET['checked'])
#     rate = request.GET['checked']
#     # user_rate_id = random.randint(1, 100000)
#     # user_id = random.randint(1, 100000)
#     # type_id = random.randint(1, 100000)
#     # rate = request.GET['checked']
#     # data = {'user_rate_id' : user_rate_id,
#     #         'user_id' : user_id,
#     #         'type_id' : type_id,
#     #         'rate' : rate}
#
#     to_db(request)
#     print('완료한 별점', rate)
#     return redirect(reverse(index))

