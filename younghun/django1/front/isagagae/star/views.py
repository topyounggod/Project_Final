from MySQLdb.cursors import DictCursor
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import *
import pymysql
from pathlib import Path
import pandas as pd
from .findNearInfras import nearInfras
import requests
import json
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
BASE_DIR = Path(__file__).resolve().parent.parent

# pymysql.install_as_MySQLdb()

# Create your views here.


def starindex(request) :
    return render(request, 'star/star_index.html')

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

        print(hospital_rate)
        print(pharmacy_rate)
        print(playground_rate)
        print(park_rate)
        print(restaurant_rate)
        print(cafe_rate)

        user = UserTable()
        user.user_id = User.objects.get(username=request.user.get_username())
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
        password='1234',
        host='127.0.0.1',
        db='isagagae',
        charset='utf8',
        port=3305
    )

    cursor = db.cursor(pymysql.cursors.DictCursor)

#     sql = "select max(r.hospital * u.hospital_rate + r.pharmacy * u.pharmacy_rate + r.playground * u.playground_rate + r.park * u.park_rate + r.restaurant * u.restaurant_rate + r.cafe * u.cafe_rate + \
# r.salon * u.salon_rate + r.deliver * u.deliver_rate + r.equip * u.equip_rate + r.sell * u.sell_rate + r.feed * u.feed_rate + r.manage * u.manage_rate) as mymax, r.lat, r.lng, r.cluster_id\
# from cluster_result as r, user_table as u where user_id = '"+ str(User.objects.get(username=request.user.get_username()))+ "' group by r.cluster_id order by mymax desc limit 5;"

    sql = \
          "select max(r.hospital * u.hospital_rate + r.pharmacy * u.pharmacy_rate + " \
          "r.playground * u.playground_rate + r.park * u.park_rate + " \
          "r.restaurant * u.restaurant_rate + r.cafe * u.cafe_rate + " \
          "r.salon * u.salon_rate + r.deliver * u.deliver_rate + " \
          "r.equip * u.equip_rate + r.sell * u.sell_rate + " \
          "r.feed * u.feed_rate + r.manage * u.manage_rate) as mymax, " \
          "r.lat lat_, r.lng lng_, cluster_id " \
          "from cluster_result r, user_table u " \
          "where user_id = '"+ str(User.objects.get(username=request.user.get_username()))+ "' "\
          "group by cluster_id " \
          "order by mymax desc " \
          "limit 3;"

    cursor.execute(sql)

    result = cursor.fetchall()
    result = pd.DataFrame(result)

    latlng = []
    for lat, lng in zip(result['lat_'], result['lng_']):
        center = [lat, lng]
        url = "https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x=" + str(lng) + "&y=" + str(lat)
        headers = {"Authorization": "KakaoAK " + "889c9d9bd1489eb337cfeb167093b9df"}
        # headers = {"Authorization": "KakaoAK " + "889c9d9bd1489eb337cfeb167093b9df"}
        api_test = requests.get(url, headers=headers)
        url_text = json.loads(str(api_test.text))
        print(url_text)
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
        latlng.append({"lat":lat, "lng":lng, "near":redpoints, "address":url_text["documents"][0]["address_name"]})
    context = {
         'latlngs': latlng
    }
    return render(request, 'star/pinpointmap.html', context=context)

