from django.conf.urls.defaults import patterns,include,url
from company import views

urlpatterns = patterns('',
        url(r'^register/$',views.register),
        url(r'^registercustomer/$',views.registercustomer),
        url(r'^registercompany/$',views.registercompany),
      
      
      ###### login /log out #######################
      
        url(r'^login/$',views.login_user),
        url(r'^logout/$',views.logout_user),
        url(r'^changepassword/$',views.change_password),
        url(r'^forgotpassword/$',views.forgot_password),
        url(r'^reset/$',views.reset_password),
        
   ############### user details ####################
        
        url(r'^customerhome/$',views.customerhome),
        url(r'^customerlist/$',views.customerlist),
        url(r'^vegcustomerlist/$',views.vegcustomerlist),
        url(r'^nonvegcustomerlist/$',views.nonvegcustomerlist),
        url(r'^companylist/$',views.companylist),
        url(r'^customerinfo/(?P<r_id>\d+)/$',views.customerinfo),
        url(r'^companyinfo/(?P<u_id>\d+)/$',views.companyinfo),
        
     ################# recipes #############################   
        
        url(r'^recipeslist/$',views.recipeslist),
        url(r'^recipesinfo/(?P<l_id>\d+)/$$',views.recipesinfo),
        url(r'^newrecipe/$',views.all_recipes),
        
     ############## vote up/vote down ################
        
        url(r'^voteup/(?P<v_id>\d+)/$',views.voteup),        
        url(r'^votedown/(?P<vd_id>\d+)/$',views.votedown),
        
     ############### events ###############################
        
        url(r'^registerevent/$',views.registerevent),
        url(r'^eventslist/$',views.eventsinfo),
        url(r'^joinevent/(?P<e_id>\d+)/$',views.joinevent),
        
        
   ################## admin ###############################
        
        url(r'^managecustomers/$',views.manage_customers),
        url(r'^customerdata/(?P<d_id>\d+)/$',views.customer_details),
        url(r'^deletecustomer/(?P<cust_id>\d+)/$',views.delete_customer),
        
        url(r'^managecompanies/$',views.manage_companies),
        url(r'^companydata/(?P<dd_id>\d+)/$',views.company_details),
        url(r'^deletecompany/(?P<comp_id>\d+)/$',views.delete_company),
        #url(r'^reviews/(?P<re_id>\d+)/$',views.re_views),
        )
