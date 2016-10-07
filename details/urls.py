from django.conf.urls import url
from .views import aboutme, contactme, sentmail

app_name ='details'
urlpatterns = [
    url('^aboutme/$',aboutme,name='aboutme'),
    url('^contactme/$',contactme, name='contactme'),
    url('^contactme/sentmail/$',sentmail, name='sentmail'),
]