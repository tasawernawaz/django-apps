# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response

from models import Author, Book


def add_author(request):
    a = Author(first_name ='tasawer',last_name ='nawaz',email ='tasawernawaz@gmail.com')
    a.save()
    a = Author.objects.all()
    # print a
    return  render_to_response('testModel.html',{'author_list':a})


def search_form_book(request):
    return render_to_response('search_form.html')


def search_book(request):
    if 'q' in request.GET and request.GET['q']:
        # message = 'You enter %r' %request.GET['q']
        q = request.GET['q']
        books = Book.objects.filter(title__icontains = q)
        return render_to_response('search_results.html',{'books':books, 'querry':q})
    else:
        message = 'You entered nothing'
    # return render_to_response(message)
    return HttpResponse(message)

