from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^menu$', 'Pantrek_app.views.menu', name='menu'),
    url(r'^$', 'Pantrek_app.views.home', name='home'),
    url(r'^company$', 'Pantrek_app.views.company', name='company'),
    url(r'^trip_summary$', 'Pantrek_app.views.trip_summary', name='trip_summary'),
    url(r'^seat$', 'Pantrek_app.views.seat', name='seat'),
    url(r'^search_results$', 'Pantrek_app.views.search_results', name='search_results'),
    url(r'^confirmation', 'Pantrek_app.views.confirmation', name='confirmation'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
