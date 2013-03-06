from django.conf.urls.defaults import patterns,include,url
from company import views

urlpatterns = patterns('',
        url(r'^register/$',views.register),
        url(r'^registercustomer/$',views.registercustomer),
        url(r'^registercompany/$',views.registercompany),
        url(r'^login/$',views.login_user),
        url(r'^logout/$',views.logout_user),
        url(r'^customerhome/$',views.customerhome),
        url(r'^customerlist/$',views.customerlist),
        url(r'^recipeslist/$',views.recipeslist),
        url(r'^recipesinfo/(?P<l_id>\d+)/$$',views.recipesinfo),
        url(r'^vegcustomerlist/$',views.vegcustomerlist),
        url(r'^nonvegcustomerlist/$',views.nonvegcustomerlist),
        url(r'^companylist/$',views.companylist),
        url(r'^newrecipe/$',views.all_recipes),
        url(r'^customerinfo/(?P<r_id>\d+)/$',views.customerinfo),
        url(r'^companyinfo/(?P<u_id>\d+)/$',views.companyinfo),
        url(r'^voteup/(?P<v_id>\d+)/$',views.voteup),        
        url(r'^votedown/(?P<vd_id>\d+)/$',views.votedown),
        url(r'^registerevent/$',views.registerevent),
        url(r'^eventslist/$',views.eventsinfo),
        url(r'^joinevent/(?P<e_id>\d+)/$',views.joinevent),
        #url(r'^participants/(?P<e_id>\d+)/$',views.joined_users),

        #url(r'^reviews/(?P<re_id>\d+)/$',views.re_views),
        )
