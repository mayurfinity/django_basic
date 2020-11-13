from django.urls import path,include
from django_app import views

app_name='django_app'

urlpatterns = [
    path('stud',views.stud,name='stud'),
    path('studuser',views.studuser,name='studuser'),
    
]