# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from js.forms import ContactForm
from django.contrib.auth import authenticate, login


def hello1(request):
    return HttpResponse("Hello")

def contact_form(request):
    form = ContactForm()
    return render_to_response('contact_form.html', {'cities':['lahore','islamabad','karachi','peshawar'], 'form': form })

def search_name(request):

    form = ContactForm(request.GET)
    return render_to_response('thanks.html',{'city':form['city']}, context_instance=RequestContext(request))

