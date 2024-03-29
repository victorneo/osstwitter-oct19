from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'osstwitter.views.home', name='home'),
    # url(r'^osstwitter/', include('osstwitter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),


    url(r'^$', 'tweets.views.index'),
    url(r'^greet/([A-Za-z-]+)/$', 'tweets.views.greet'),
    url(r'^greet/$', 'tweets.views.index'),
    url(r'^tweets/$', 'tweets.views.get_tweets'),
)
