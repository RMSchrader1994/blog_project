from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^posts/', post_list, name='post_list'),
    url(r'^create/', create_posts, name='create_posts'),
    url(r'delete/(\d+)$', delete_post, name="delete_post"),
    url(r'edit/(\d+)$', edit_post, name="edit_post"),
    url(r'^post/(\d+)', post_detail, name='post_detail'),
]