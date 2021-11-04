import pymysql

db = pymysql.connect(
    user='root',
    passwd='1234',
    host='127.0.0.1',
    db='TEST',
    charset='utf8',
    port = 3306,
)


# Dict Insert #

cursor = db.cursor(pymysql.cursors.DictCursor)

# [dict형 자료] insert
insert_data = [{'a':1,'b':2},{'a':1,'b':2}]

insert_sql = "INSERT INTO star_rate VALUES (%(a)s, %(b)s);"
# a,b,c,d는 컬럼 이름 / s : string

cursor.executemany(insert_sql, insert_data)

db.commit()