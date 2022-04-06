from django.urls import path

from . import views
from . import api

app_name = 'poor_mans_twitter'

urlpatterns = [
    path('', views.index, name='index'),
    
    path('api/tweets/store', api.store, name='tweets_store'),
    path('api/tweets', api.index, name='tweets_index'),
]