from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^posts', get_posts, name="get_posts"),
    url(r'^create', create_posts, name="create_posts"),
]