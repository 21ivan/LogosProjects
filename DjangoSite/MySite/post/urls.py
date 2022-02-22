from django.conf.urls import url
from post.views import *
from . import views
from django.urls import path

urlpatterns = [
    path('', home_page),
    path('create/', post_create),
    path('delete/', post_delete),
    path('detail/<int:id>/', post_detail),
    path('update/<int:id>/', post_update)
]