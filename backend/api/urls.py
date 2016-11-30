from __future__ import unicode_literals
from django.conf.urls import include, url

from api import views

auth_urls = [
    url(r'^login/$', views.userLogin, name='user-login'),
    url(r'^signup/$', views.userSignup, name='user-singup'),
    url(r'^$', views.userList, name='user-list')
]

tours_urls = [
    url(r'^(?P<tour_id>.*)/$', views.tourdetail ,name='tour-detail'),
    url(r'^$', views.tourlist, name='tour-list')
]

history_urls = [
    url(r'^(?P<user_id>.*)/$', views.historydetail ,name='history-detail'),
    url(r'^$', views.historylist, name='history-list')
]

urlpatterns = [
    url(r'^auth/', include(auth_urls)),
    url(r'^tours/', include(tours_urls)),
    url(r'^history/', include(history_urls)),
]
