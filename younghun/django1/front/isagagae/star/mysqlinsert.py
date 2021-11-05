#

import pymysql
import pandas as pd
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
      "where user_id = '1'" \
      "order by sum desc " \
      "limit 3)" \
      "a;"

cursor.execute(sql)

result = cursor.fetchall()
result = pd.DataFrame(result)
print(result)