from django.shortcuts import render_to_response
from forms import RegisterCustomerForm
from forms import RegisterCompanyForm
from forms import LoginForm
from forms import RecipesForm,ReviewsForm,EventsForm
from forms import ChangePassword,ForgotPassword,ResetForm
from company.models import Customer
from company.models import Company  
from company.models import UserProfile,Recipes,Reviews,Events,JoinEvent
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django import http
from django.contrib.auth import authenticate, login ,logout
from django.core.urlresolvers import reverse
from django.template import RequestContext

from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

def home(request):
    return render_to_response('home.html',locals())


def register(request):
    return render_to_response('register.html')


def registercustomer(request):
    print request.method
    if request.method == 'POST':
        print "inside post if "
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            print "inside form valid"
            user=User.objects.create(
            username = form.cleaned_data['username'],
            first_name = form.cleaned_data['first_name'],
            last_name = form.cleaned_data['last_name'],
            email = form.cleaned_data['email'],
            password = form.cleaned_data['password'], 
            )
            user.repassword = form.cleaned_data['repassword']
            if user.repassword != user.password:
                state="password and repassword not matching "
                eform=form
                return render_to_response('customers_reg.html',locals())

            user.set_password(str(form.cleaned_data['password']))
            user.save()

            customer=Customer.objects.create(
            customer=user,
            address=form.cleaned_data['address'],
            contact_no=form.cleaned_data['contact_no']
            )

            customer.save()
            current_user=UserProfile.objects.create(
                   user=user,
                   user_type="customer",
                   )
            current_user.save()
            #send_mail('Registeration-Foodline', ' Welcome to foodline ', 'foodline77@gmail.com', [user.email])

            return HttpResponseRedirect('/foodline/login/')
        else:
            state="Please fill the form correctly"
            reg_form=form
            return render_to_response('customer_reg.html',locals())
    else:
        state="Welcome,fill the form to register"
        form=RegisterCustomerForm()
        return render_to_response('customer_reg.html',locals())
        
        
        
        
        

def registercompany(request):
    print request.method
    if request.method == 'POST':
        print "inside post if "
        form = RegisterCompanyForm(request.POST)
        if form.is_valid():
            print "inside form valid"
            user=User.objects.create(
            username = form.cleaned_data['username'],
            first_name = form.cleaned_data['first_name'],
            last_name = form.cleaned_data['last_name'],
            email = form.cleaned_data['email'],
            password = form.cleaned_data['password'],                                          
            )
            user.repassword = form.cleaned_data['repassword']
            
            if user.repassword != user.password:
                state="password and repassword not matching "
                eform=form
                return render_to_response('company_reg.html',locals())
                
            user.set_password(str(form.cleaned_data['password']))
            user.save()

            company=Company.objects.create(
            company=user,
            company_name=form.cleaned_data['company_name'],
            address=form.cleaned_data['address'],
            contact_no=form.cleaned_data['contact_no'],
            cuisine = form.cleaned_data['cuisine'],
            home_delivery = form.cleaned_data['home_delivery'],
            lodging = form.cleaned_data['lodging'],

            )

            company.save()
            
            current_user=UserProfile.objects.create(
                   user=user,
                   user_type="company",
                   )
            current_user.save()
            #send_mail('Registeration -Foodline', ' Welcome to foodline, ', 'foodline77@gmail.com', [user.email])
            
            return HttpResponseRedirect('/foodline/login/')
        else:
            state="Please fill the form correctly"
            reg_form=form
            return render_to_response('company_reg.html',locals())
    else:
        state="Welcome,fill the form to register"
        form=RegisterCompanyForm()
        return render_to_response('company_reg.html',locals())

######################### recipes ######################################3         


def all_recipes(request):
    if request.method == 'POST':
        form=RecipesForm(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('home.html',locals())
        else:
            rform=form
            return render_to_response('recipes.html',locals())
    else:
        form=RecipesForm()
        return render_to_response('recipes.html',locals())


def recipeslist(request):
    recipes_data=Recipes.objects.all()
    return render_to_response('displayrecipes.html',locals())
    

def recipesinfo(request, l_id):
    recipes_data=Recipes.objects.get(id=l_id)
    return render_to_response('recipesinfo.html',locals())
        
########################### login / logout ###################################

def login_user(request):
  
    username = password = ''
    if request.method== 'POST':
        form=LoginForm(request.POST)                
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return render_to_response('home.html',locals())
            else:
                request_user=UserProfile.objects.get(user=user)
            #print request_user.user_type            
                if request_user.user_type=="customer":
                    return HttpResponseRedirect('/foodline/customerhome/')
                else:
                    return HttpResponseRedirect('/foodline/companylist/')
        else:
            form=LoginForm()
            return render_to_response('login.html',locals())
    else:
        form=LoginForm()
        return render_to_response('login.html',locals())



def logout_user(request):
    logout(request)
    return render_to_response('home.html',locals())
    
def customerhome(request):
    company_data = Company.objects.all()
    return render_to_response('customerhome.html',locals()) 
        
    
def customerlist(request):
    company_data = Company.objects.all()
    return render_to_response('customer.html',locals()) 
    
def vegcustomerlist(request):
    company_data = Company.objects.filter(cuisine='Veg')
    print company_data
    return render_to_response('customer.html',locals())       

def nonvegcustomerlist(request):
    company_data = Company.objects.filter(cuisine='NonVeg')
    print company_data
    return render_to_response('customer.html',locals()) 
  
def companylist(request):
    customer_data=Customer.objects.all()
    return render_to_response('company.html',locals())
    
def customerinfo(request,r_id):
    company_data = Company.objects.get(id = r_id )
    print company_data
    return render_to_response('customerinfo.html',locals())


################### voteup / vote down #########################################


def voteup(request,v_id):
    review_data = Reviews.objects.get(id =v_id )
    review_data.voteup = review_data.voteup + 1;
    review_data.save()
    return render_to_response('reviews.html',locals())
    
def votedown(request,vd_id):
    review_data = Reviews.objects.get(id = vd_id )
    review_data.votedown = review_data.votedown + 1;
    review_data.save()
    return render_to_response('reviews.html',locals())
    

 
def re_views(request,re_id):

    if request.method=="POST":
        form = ReviewsForm(request.POST)
        if form.is_valid():
            rev=Reviews.objects.create(
            reviews=form.cleaned_data['reviews'],
            )
            rev.save()
            review_data = Reviews.objects.get(id=re_id)
            return render_to_response('customerinfo.html',locals())
        
    else:
        form=ReviewsForm()
        return render_to_response('customerinfo.html',locals()) 
        
        
        
        
def companyinfo(request,u_id):
    customer_data = Customer.objects.get(id = u_id )
    print customer_data
    return render_to_response('companyinfo.html',locals())    
 
########## events ############################################################3

def registerevent(request):
    if request.method== 'POST':
        form=EventsForm(request.POST)
        if form.is_valid():
            events=Events.objects.create(
            rest=Company.objects.get(company=request.user),
            event_name=form.cleaned_data['event_name'],
            event_date=form.cleaned_data['event_date'],
            event_time=form.cleaned_data['event_time'],
            )
            events.save()
            return HttpResponseRedirect('/')
        else:    
            state="please fill in all fields properly"
            eform=form
            return render_to_response('event_reg.html',locals())
    else:
        state="Welcome,fill the form to register"
        form=EventsForm()
        return render_to_response('event_reg.html',locals())


@login_required   
def eventsinfo(request):
    event_data=Events.objects.all()
    user_part_of = []
    print event_data
    for event in event_data:
        has_joined = JoinEvent.objects.filter(participant = request.user, event= event)
        s = {"id":event.id, "event_name": event.event_name, "event_date":event.event_date, "event_time": event.event_time, "location":event.rest.company_name}
        if has_joined:
            s["is_part"] = True
        else :
            s["is_part"] = False
        user_part_of.append(s)
    print user_part_of
    return render_to_response('events.html',locals())


@login_required
def joinevent(request,e_id):
    if request.user.is_authenticated:
        jevent=JoinEvent.objects.create(
                participant=request.user,
                event=Events.objects.get(id=e_id),
                )
        jevent.save()
        return HttpResponseRedirect('/foodline/eventslist')
        #users_data = JoinEvent.objects.all()
        #return render_to_response('joinedusers.html',locals())
    else:
        return HttpResponseRedirect('/foodline/register/')


########################### ADMIN  ####################################################3    

def manage_customers(request):
    customer_data=Customer.objects.all()
    return render_to_response('manage_customers.html',locals())
 

def customer_details(request,d_id):
    customer_data=Customer.objects.get(id = d_id)
    return render_to_response('cust_data.html',locals())


def delete_customer(request,cust_id):
    customer_data=Customer.objects.get(id=cust_id).delete()
    return HttpResponseRedirect('/foodline/managecustomers/')
    
            
def manage_companies(request):
    company_data=Company.objects.all()
    return render_to_response('manage_companies.html',locals())    
    
    
def company_details(request,dd_id):
    company_data=Company.objects.get(id = dd_id)
    return render_to_response('comp_data.html',locals())   
    
def delete_company(request,comp_id):
    company_data=Company.objects.get(id=comp_id).delete()
    return HttpResponseRedirect('/foodline/managecompanies/')

##########################################################################################

def forgot_password(request):
    if request.method=="POST":
        form=ForgotPassword(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            print username
            user=User.objects.get(username=username)
            print user
            if user is not None:
                link="http://127.0.0.1:8000/foodline/reset/"
                send_mail("RESET PASSWORD",link,"foodline77@gmail.com",[user.email])
                return HttpResponseRedirect('/foodline/login/')
            else:
                return render_to_response('home.html',locals())
        else:
            reg_form=form
            return render_to_response('forgot_password.html',locals())
    else:
        form=ForgotPassword()
        state="Please enter Username"
        return render_to_response('forgot_password.html',locals())
                       



def reset_password(request):
    if request.method=="POST":
        form=ResetForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            user=User.objects.get(username=username)
            print user
            user.set_password(str(form.cleaned_data['password']))
            user.save()
            return HttpResponseRedirect('/foodline/login/')
        else:
            reg_form=form
            return render_to_response('re_password.html',locals())
    else:
        form=ResetForm()
        state="Please enter your new password"
        return render_to_response('re_password.html',locals())
               

def change_password(request):
    if request.method=="POST":
        form=ChangePassword(request.POST)
        if form.is_valid():
            register_user=User.objects.get(username=request.user.username)
            register_user.set_password(str(form.cleaned_data['password']))
            register_user.save()
            return HttpResponseRedirect('/foodline/login/')
        else:
            state="please enter a new password"
            return render_to_response('reset.html',locals())
    else:
        form=ChangePassword()
        state="Enter a New Password"
        return render_to_response('reset.html',locals())
 

