from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^posts/', post_list, name='post_list'),
    url(r'^create/', create_posts, name='create_posts'),
    url(r'^post/(\d+)', post_detail, name='post_detail'),
]