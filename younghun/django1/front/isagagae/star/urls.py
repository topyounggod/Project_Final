from django.urls import path
from . import views
app_name = 'star'
urlpatterns = [
    path('',views.starindex,name='star_index'),
    path('pinmap', views.showpinmap, name='pinmap'),
]