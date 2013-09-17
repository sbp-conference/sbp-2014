from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
# Create your views here.

def home(request, **kwargs):
    context = { 'page_title': 'SBP 2013',
                'name': 'home',
                'fonts': ''}


    return render_to_response("base/index.html", context, RequestContext(request))

def about(request, **kwargs):
    context = { 'page_title': 'About',
                'name': 'about',
                'fonts': ''}
    return render_to_response("base/page.html", context, RequestContext(request))

def cfp(request, **kwargs):
    context = { 'page_title': 'Call for Proposals',
                'name': 'home',
                'fonts': ''}
    return render_to_response("base/cfp.html", context, RequestContext(request))

def committee(request, **kwargs):
    context = { 'page_title': 'Committee',
                'name': 'home',
                'fonts': ''}
    return render_to_response("base/committee.html", context, RequestContext(request))
