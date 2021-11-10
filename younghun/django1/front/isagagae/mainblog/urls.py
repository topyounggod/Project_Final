from django.urls import path, include
from . import views
from .views import CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',views.index,name='index'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('service/',include('star.urls',namespace='starfin')),
    # path('/service/showpinmap/',include('star.urls',namespace='showpinmap')),
    ]