import pymysql

db = pymysql.connect(
    user='root',
    passwd='0000',
    host='127.0.0.1',
    db='TEST',
    charset='utf8',
    port = 3306,
)


# Dict Insert #

cursor = db.cursor(pymysql.cursors.DictCursor)

# [dict형 자료] insert
insert_data = [{'a':1,'b':2,'c':3,'d':4},{'a':1,'b':2,'c':3,'d':4}]

insert_sql = "INSERT INTO TEST VALUES (%(a)s, %(b)s, %(c)s, %(d)s);"

# a,b,c,d는 컬럼 이름 / s : string
cursor.executemany(insert_sql, insert_data)

db.commit()

# infra_type 넣기

cursor = db.cursor(pymysql.cursors.DictCursor)

insert_data = [{'a':1,'b':'Health'},{'a':2,'b':'Play'}, {'a':3,'b':'Food'},
               {'a':4,'b':'Beauty'},{'a':5,'b':'Life'}, {'a':6,'b':'Care'}]

insert_sql = "INSERT INTO infra_type VALUES (%(a)s, %(b)s);"

# a,b,c,d는 컬럼 이름 / s : string
cursor.executemany(insert_sql, insert_data)

db.commit()
