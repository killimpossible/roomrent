from django.conf.urls.defaults import *


urlpatterns = patterns('',
                       (r'^to_room_add/$','room_manage.views.to_room_add'),
                       (r'^room_add/$','room_manage.views.room_add'),
                       (r'^detail/$','room_manage.views.room_detail'),
                       (r'^room_del/$','room_manage.views.room_del'),
)
