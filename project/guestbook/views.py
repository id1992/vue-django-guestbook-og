from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .models import Guestbook
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
import json

# Create your views here.
def index(request):
    '''
    render(request, template_name, context=None, content_type=None, status=None, using=None)
    - Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.
    '''
    return render(request, 'index.html')

def guestbooks(request):
    guestbooks = Guestbook.objects.all().values('guestbook_id', 'guestbook_name', 'guestbook_text')
    guestbooks_list = list(guestbooks)

    return JsonResponse({
        'guestbooks': guestbooks_list
    })

def create_guestbook(request):
    param = json.loads(request.body.decode('utf-8'))
    name = param.get("name")
    text = param.get('text')

    guestbook = Guestbook(guestbook_name = name, guestbook_text = text);
    guestbook.save();

    return HttpResponse(request)

def edit_guestbook(request, guestbook_id):
    param = json.loads(request.body.decode('utf-8'))
    modified_name = param.get("name")
    modified_text = param.get('text')

    guestbook = Guestbook.objects.get(pk=guestbook_id)
    guestbook.guestbook_name = modified_name
    guestbook.guestbook_text = modified_text
    guestbook.save(); 

    return HttpResponse(request)

def remove_guestbook(request, guestbook_id):
    guestbook = Guestbook.objects.get(pk=guestbook_id)
    guestbook.delete()
    return HttpResponse(request)

'''
restful하게 짠다면?

def guestbook(request, id):
    switch(request.method)
        # GET 동작
        # POST 동작
        # PUT 동작
        # DELETE 동작
'''