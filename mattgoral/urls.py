from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mattgoral.views.home', name='home'),
    url(r'^work/$', 'mattgoral.views.work'),
    url(r'^resume/$', 'mattgoral.views.resume'),
    url(r'^about/$', 'mattgoral.views.about'),
    url(r'^contact/$', 'mattgoral.views.contact'),
    # url(r'^mattgoral/', include('mattgoral.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^jewelry/$', 'jewelry.views.all'),
    url(r'^jewelry/(?P<item_id>\d+)/$', 'jewelry.views.detail'),
    url(r'^jewelry/earrings/$', 'jewelry.views.earrings'),
    url(r'^jewelry/bracelets/$', 'jewelry.views.bracelets'),
    url(r'^jewelry/rings/$', 'jewelry.views.rings'),
    url(r'^jewelry/necklaces/$', 'jewelry.views.necklaces'),
    url(r'^jewelry/about/$', 'jewelry.views.about'),
    
    url(r'^bar/$', 'bar.views.home'),
    #url(r'^jewelry/(?P<item_id>\d+)/$', 'bar.views.menu'),
)
