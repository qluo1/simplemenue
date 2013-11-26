from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'thesite.views.home', name='home'),
    # url(r'^thesite/', include('thesite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'bootstrap.views.index',name='Home'),
    url(r'^product$', 'bootstrap.views.product',name='Product'),
    url(r'^services$', 'bootstrap.views.services',name='Services'),
    url(r'^contact$', 'bootstrap.views.about',name='Contact'),
    url(r'^about$', 'bootstrap.views.about',name='About'),
    ## django auth
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',name='Login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',name='Logout'),
    url(r'^accounts/profile/$', 'bootstrap.views.profile',name='Profile'),
)
