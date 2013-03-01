from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
               url(r'^$','company.views.home'),
               url(r'^foodline/',include('company.urls')),
              
              
        
)


