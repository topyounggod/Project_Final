from django.urls import path,include
from . import views
from .views import showpinmap
app_name = 'star'
urlpatterns = [
    path('',views.starindex,name='star_index'),
    path('pinmap', views.showpinmap, name='showpinmap'),
    # path('user/savestar/', views.savestar, name='savestar'),
]