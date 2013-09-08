from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
# Create your views here.

def home(request, **kwargs):
    context = { 'page_title': 'django-snapbook',
                'name': 'home',
                'fonts': ''}


    return render_to_response("base/index.html", context, RequestContext(request))

def about(request, **kwargs):
    context = { 'page_title': 'django-snapbook',
                'name': 'home',
                'fonts': ''}
    return render_to_response("base/index.html", context, RequestContext(request))
