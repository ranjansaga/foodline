from django.shortcuts import render_to_response
from django import template
def home(request):
    c=template.Context({'title':'Food Line'})
    return render_to_response('home.html',c)

