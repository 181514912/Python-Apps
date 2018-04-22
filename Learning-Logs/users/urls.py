# defining url patterns for users app
from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

app_name='users'
urlpatterns=[
    url(r'^login/$',login,{'template_name':'users/login.html'},name='login'),   # login page
    url(r'^logout/$',views.logout_view,name='logout'),  # logout page
    url(r'^register/$',views.register,name='register'), # registration page
]