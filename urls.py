from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       (r'^$','web.views.index'),
                       (r'^needLogin/$', 'web.views.needLogin'),
                       (r'^user/',include('RoomRent.user_manage.urls')),
                       (r'^room/',include('RoomRent.room_manage.urls')),
    # Example:
    # (r'^RoomRent/', include('RoomRent.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
)
