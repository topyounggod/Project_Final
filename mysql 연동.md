### mysql 연동

```python
# 가상환경 잡기 - pycharm

# 터미널 열기
# pymysql 설치
pip install pymysql

# cmd 접속
mysql -u root -p -P3305
1234

show databases;
use test; #(데이터베이스 사용)

# 테이블명 : test
CREATE TABLE test(
id INT,
LOCAL_CODE INT,
DATE_CODE INT,
PRICE INT,
);

# 테이블명 : infra_type
CREATE TABLE infra_type(
id INT,
type VARCHAR(20)
);

```



```python
# 최상단 프로젝트 폴더 하위 파일로 function.py 생성

import pymysql

db = pymysql.connect(
    user='root',
    passwd='1234',
    host='127.0.0.1',
    db='TEST',
    charset='utf8',
    port = 3305,
)


# Dict Insert #

cursor = db.cursor(pymysql.cursors.DictCursor)

# [dict형 자료] insert 
insert_data = [{'a':1,'b':2,'c':3,'d':4},{'a':1,'b':2,'c':3,'d':4}]

insert_sql = "INSERT INTO TEST VALUES (%(a)s, %(b)s, %(c)s, %(d)s);"
# a,b,c,d는 컬럼 이름 / s : string

cursor.executemany(insert_sql, insert_data)

db.commit()

# Run 하기!

#insert_data = [list형자료] ex)[['a',1],['b',3]]
#insert_sql = "INSERT INTO `테이블명` VALUES (%s, %s);"
#cursor.executemany(insert_sql, insert_data) 
#db.commit()


#조회하기(dataframe형으로 변환하여 확인)
#sql = "SELECT * FROM 테이블;"
#cursor.execute(sql)
#result = cursor.fetchall()
#result = pd.DataFrame(result)
#print(result)

```



```python
# Django와 mysql 연결

# 커넥터 설치 
pip install mysqlclient

# settings.py있는 폴더에서 my_settings.py 파일을 생성한 후 

DATABASES = {
    'default':{
    'ENGINE':'django.db.backends.mysql',
    'NAME':'TEST', #db이름
    'USER':'root',
    'PASSWORD':'1234',
    'HOST':'127.0.0.1',
    'PORT':'3305',
    }
}
SECRET_KEY = 'settings.py 파일 안에 있는 secret key 복사'

# settings.py 수정

from . import my_settings

settings.py내에 이미 존재하는 databases,secretkey를 주석처리하고
DATABASES = my_settings.DATABASES
SECRET_KEY = my_settings.SECRET_KEY
로 대체한다

#확인
python manage.py inspectdb로 확인

```



```python
# models.py로 이동

class Test(models.Model):
    id = models.IntegerField(db_column='ID', primary_key = True)
    # 컬럼명이 id여서 기본키로 인식했음 -> 옵션을 primary_key = True로 줌
    local_code = models.IntegerField(db_column='LOCAL_CODE', blank=True, null=True)  
    date_code = models.IntegerField(db_column='DATE_CODE', blank=True, null=True) 
    price = models.IntegerField(db_column='PRICE', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'test'

# python terminal
>python manage.py makemigrations
>python manage.py migrate
>python manage.py runserver

############################################
# views.py 수정
from django.shortcuts import render, HttpResponse
from .models import Test

# Create your views here.

def showblog(request) :
    a = Test.objects.all()
    return render(request, 'index.html', {'a':a})

############################################
# index.html 파일 수정 
{%for i in a%} # Test 테이블의 모든 값을 가져와서 a라는 변수에 넣었음 (views.py에서)
{{i.price}} # Test 테이블의 모든 값 중 address 컬럼에 해당하는 값을 출력
{%endfor%}
```



```python
# form 태그 만들어서 input 값 받기
# form : 사용자가 입력한 문자열을 서버로 전달하기 위해 사용

# html body 내부 중 아무데나 만들기

<div class = "messageDiv">

# memo 작성 후 버튼 누르면 http://127.0.0.1:8000/memotest/ < 이 경로로 데이터 전달
	<form action = "./memotest/" method = "POST">{% csrf_token %} 

# POST 방식 사용할 때 : {% csrf_token %} 필수로 적어주어야 함

	<div class = "input-group">
		<input id = "inputContent" name = "inputContent" type="text" class = "form-control" placeholder = "적어주세요">
		<span class = "input-group-btn">
			<button class = "btn btn-default" type="submit">메모하기!</button>
		</span>
	</div>
	</form>

</div>

```

```python
# urls.py 변경
from django.contrib import admin
from django.urls import path
import mainblog.views

urlpatterns = [
    path('', mainblog.views.showblog, name='showblog'),
    path('admin/', admin.site.urls),
    path('memotest/', mainblog.views.memotest, name = 'memotest')
]


# mainblog > views.py
from django.shortcuts import render
from .models import Test
from django.http import HttpResponse
# Create your views here.

def showblog(request) :
    a = Test.objects.all()
    return render(request, 'index.html', {'a':a})

def memotest(request) :
    return HttpResponse('memotest임!')


```

#### request에서 name을 이용해서 input 태그 안에 있는 문자열 받아오기

```python
# mainblog > views.py

from django.shortcuts import render
# from .models import Test
from django.http import HttpResponse
from .models import *
# Create your views here.

def showblog(request) :
    a = Test.objects.all()
    return render(request, 'index.html', {'a':a})

def memotest(request) :
    user_input_str = request.POST['inputContent']
     # 사용자 인풋값이 new_memo라는 변수에 저장됨
    new_memo = Memo(content = user_input_str)
    new_memo.save()
    return HttpResponse('memotest임! =>'+user_input_str)

# mainblog > models.py
class Memo(models.Model) :
    content = models.CharField(max_length=255)
    
# terminal #
# 데이터베이스에 전해 줄 초안, 설계도, 작업 지시서 등과 비슷한 역할
python manage.py makemigrations
# 데이터베이스에서 실제로 테이블 만들기
python manage.py migrate
# 데이터베이스에 접근해서 테이블 만들어졌는지 확인
python manage.py dbshell
show databases;
use test;
show tables;
# 프로젝트이름_모델이름 으로 형성된 것 확인할 수 있음 

# 들어간 메모 확인하기
select * from mainblog_memo;

```



#### 메모 저장 후 메인페이지로 돌아가기

```python
# mainblog > views.py

from django.shortcuts import render, redirect
# from .models import Test
from django.http import HttpResponse
from django.urls import reverse
from .models import *
# Create your views here.

def showblog(request) :
    a = Test.objects.all()
    memos = Memo.objects.all()
    content = {'memos' : memos}
    # return render(request, 'index.html', {'a': a})
    return render(request, 'index.html', {'a':a, 'memos':memos})

def memotest(request) :
    user_input_str = request.POST['inputContent']
    # 사용자 인풋값이 new_memo라는 변수에 저장됨
    new_memo = Memo(content = user_input_str)
    new_memo.save()
    return redirect(reverse('showblog'))
    # return HttpResponse('memotest임! =>'+user_input_str)
    
# index.html 수정
<!-- input 값 보여주기 test -->
<div class = "memoDiv">
<ul class = "list_group">
{% for memo in memos %}
<form action="" method="GET">
<div class="input-group" name="memo1">
<li class = "list-group-item">{{ memo.content }}</li>
<input type = "hidden" id = "memoNum" name = "memoNum" value = "{{ memo.id }}">
<span class = "input-group-addon">
<button type="submit" class = "custom-btn btn btn-danger">완료</button>
</span>
</div>
</form>
{% endfor %}
</ul>
</div>

# {{ }} : 사용자에게 직접 보여 주는 값 
```

#### 메모 삭제 

```python
# index.html에서 delete action 추가
<!-- input 값 보여주기 test -->
<div class = "memoDiv">
<ul class = "list_group">
{% for memo in memos %}
<form action="./deleteMemo" method="GET">
<div class="input-group" name="memo1">
<li class = "list-group-item">{{ memo.content }}</li>
<input type = "hidden" id = "memoNum" name = "memoNum" value = "{{ memo.id }}">
<span class = "input-group-addon">
<button type="submit" class = "custom-btn btn btn-danger">완료</button>
</span>
</div>
</form>
{% endfor %}
</ul>
</div>

# urls.py 수정
from django.contrib import admin
from django.urls import path
import mainblog.views

urlpatterns = [
    path('', mainblog.views.showblog, name='showblog'),
    path('admin/', admin.site.urls),
    path('memotest/', mainblog.views.memotest, name = 'memotest'),
    path('deleteMemo/', mainblog.views.doneMemo, name = 'deleteMemo')
]

# mainblog > views.py
from django.shortcuts import render, redirect
# from .models import Test
from django.http import HttpResponse
from django.urls import reverse
from .models import *
# Create your views here.

def showblog(request) :
    a = Test.objects.all()
    memos = Memo.objects.all()
    content = {'memos' : memos}
    # return render(request, 'index.html', {'a': a})
    return render(request, 'index.html', {'a':a, 'memos':memos})

def memotest(request) :
    user_input_str = request.POST['inputContent']
    # 사용자 인풋값이 new_memo라는 변수에 저장됨
    new_memo = Memo(content = user_input_str)
    new_memo.save()
    return redirect(reverse('showblog'))
    # return HttpResponse('memotest임! =>'+user_input_str)

def doneMemo(request) :
    done_memo_id = request.GET['memoNum']
    print('완료한 memo의 id', done_memo_id)
    memo = Memo.objects.get(id = done_memo_id)
    memo.delete()
    return redirect(reverse('showblog'))


```

