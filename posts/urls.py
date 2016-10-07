from django.conf.urls import url
from .views import *

app_name ='posts'

urlpatterns =[
    url(r'^$', index, name='index'),
    url(r'^posts/(?P<post_url>.+)$', showmore, name='showmore'),
    url(r'^vote/$', support, name='support'),
    url(r'^comment_model/$', comment_model, name='comment_model'),
    url(r'^comment/$',comment, name='comment'),
]
