# defines url patterns for learning_logs
from django.conf.urls import url
from . import views

app_name='learning_logs'
urlpatterns=[
    url(r'^$',views.index,name='index'),    # home page
    url(r'^topics/$',views.topics,name='topics'),   # show all topics
    url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),   # detail page for a single topic
    url(r'^new_topic/$',views.new_topic,name='new_topic'),
    url(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'), # adding a new entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry,name='edit_entry'), # editing an entry
]