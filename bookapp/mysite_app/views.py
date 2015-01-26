# Create your views here.
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
import datetime
from django.template import RequestContext
from django.template.loader import get_template
from mysite_app.forms import ContactForm

def hello(request):
    return render_to_response("testCSS/index.html")


def current_time(request):
    html = get_template("test.html")
    # t = Template(html)
    # c = Context({'itemList':['lahore','Islamabad'],'date':datetime.datetime.now})
    # t.render(c)
    return render_to_response('test.html',{'itemList':['lahore','Islamabad'],'date':datetime.datetime.now})


def meta_view(request):
    values = request.META.items()
    values.sort()
    html = []
    for k,v in values:
        html.append("<tr><td> %s </td> <td> %s </td></tr>" %(k,v))

    html= HttpResponse("<html><body> <table>>%s</table> </body></html>" %'\n'.join(html))
    return html


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # send_mail(
            #     cd['subject'],
            #     cd['message'],
            #     cd.get('e-mail', 'noreply@example.com'),
            #     ['siteowner@example.com'],)
            return HttpResponseRedirect('/thanks/')

    else:
        form = ContactForm( initial={'subject':'I love ur Site'})
    return render_to_response('contact.html', {'form': form}, context_instance=RequestContext(request))



def thanks(request):
    return render_to_response('thanks.html')