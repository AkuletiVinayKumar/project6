from app1.views import * 
from django.urls import path
app_name='something'
urlpatterns=[
    path('first_app1/',first_app1,name='first_app1')
]