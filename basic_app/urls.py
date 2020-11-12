from django.urls import path,include
from basic_app import views

app_name='basic_app'

urlpatterns = [
    path('index',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.userlogin,name='login'),

]
