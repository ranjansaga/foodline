from django import forms
from django.forms import ModelForm
from company.models import Recipes
from company.models import CustomerChoice
from django.forms.fields import ChoiceField

TYPE = ( ('Veg', 'Veg'),
         ('NonVeg', 'NonVeg'),
         ('Punjabi', 'Punjabi'),
       )
       


class RegisterCustomerForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password= forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField()
    contact_no=forms.IntegerField()


class RegisterCompanyForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password= forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)
    company_name=forms.CharField(max_length=100)
    #rating=forms.FloatField()
    address=forms.CharField()
    home_delivery=forms.NullBooleanField()
    lodging=forms.NullBooleanField()
    cuisine = forms.ChoiceField(choices = TYPE)
    contact_no=forms.IntegerField()
    

class RecipesForm(ModelForm):
    class Meta:
        model =Recipes


class CustomerChoiceForm(forms.Form):
    cuisine=forms.ChoiceField(choices = TYPE)
    home_delivery=forms.NullBooleanField()
    lodging=forms.NullBooleanField()

                                 

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password= forms.CharField(widget=forms.PasswordInput)
    
class ReviewsForm(forms.Form):
    reviews = forms.CharField()
    

class EventsForm(forms.Form):
    event_name=forms.CharField(max_length=30)
    event_date=forms.DateField()
    event_time=forms.CharField()
    
    
class ChangePassword(forms.Form):
    password= forms.CharField(widget=forms.PasswordInput)
    
class ForgotPassword(forms.Form):
    username = forms.CharField(max_length = 30)
    
class ResetForm(forms.Form):
    username = forms.CharField(max_length = 30)
    password = forms.CharField(widget=forms.PasswordInput)


