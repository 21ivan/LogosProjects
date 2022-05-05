
from post.views import *
from django.urls import path

app_name = 'post'
urlpatterns = [
    path('', post_list, name='post_list'),
    path('create/', post_create, name='post_create'),
    path('delete/<int:id>/', post_delete, name='post_delete'),
    path('detail/<int:id>/', post_detail, name='post_detail'),
    path('update/<int:id>/', post_update, name='post_update')
]
