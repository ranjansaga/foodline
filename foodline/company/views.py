from django.shortcuts import render_to_response
from forms import RegisterCustomerForm
from forms import RegisterCompanyForm
from forms import LoginForm
from forms import RecipesForm,ReviewsForm
from company.models import Customer
from company.models import Company  
from company.models import UserProfile,Recipes,Reviews
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django import http
from django.contrib.auth import authenticate, login ,logout
from django.core.urlresolvers import reverse
from django.template import RequestContext
def home(request):
    return render_to_response('home.html')


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

            
            return HttpResponseRedirect('/foodline/login/')
        else:
            state="Please fill the form correctly"
            reg_form=form
            return render_to_response('company_reg.html',locals())
    else:
        state="Welcome,fill the form to register"
        form=RegisterCompanyForm()
        return render_to_response('company_reg.html',locals())



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
        



def login_user(request):
  
    username = password = ''
    if request.method== 'POST':
        form=LoginForm(request.POST)                
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
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
 
   
   

