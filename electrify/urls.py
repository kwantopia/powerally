from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'electrify.views.home', name='home'),
    # url(r'^electrify/', include('electrify.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'main.views.home', name='home'),
    url(r'^dashboard/$', 'main.views.dashboard', name='dashboard'),
    url(r'^about/$', 'main.views.about', name='about'),
)
