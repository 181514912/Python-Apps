# defines url patterns for learning_logs
from django.conf.urls import url
from . import views

app_name='learning_logs'
urlpatterns=[
    url(r'^$',views.index,name='index'),    # home page
    url(r'^topics/$',views.topics,name='topics'),   # show all topics
    url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),   # detail page for a single topic
]