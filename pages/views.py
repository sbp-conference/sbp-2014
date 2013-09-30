from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from models import Page

# Create your views here.

def home(request, **kwargs):
    context = { 'page_title': 'SBP 2013',
                'name': 'home',
                'fonts': ''}


    return render_to_response("base/index.html", context, RequestContext(request))

def cfp(request, **kwargs):
    context = { 'page_title': 'Call for Papers',
                'name': 'home',
                'fonts': ''}
    return render_to_response("base/cfp.html", context, RequestContext(request))

def committee(request, **kwargs):
    context = { 'page_title': 'Committee Members',
                'name': 'home',
                'fonts': ''}
    return render_to_response("base/committee.html", context, RequestContext(request))

def tbd(request, **kwargs):
    page_title = kwargs.get('page')

    try:
        query = Page.objects.get(url=page_title)
        page_title = query.page_title
        stringoftext = query.main_article
        sidebar = query.sidebar
    except:
        page_title = page_title
        stringoftext = "<div class=\"title\"><h3>Under Construction</h3></div><p>This page is currently under construction.</p>"
        sidebar = ""

    context = { 'page_title': page_title,
                'page_contents': stringoftext,
                'fonts': ''}
    return render_to_response("base/page.html", context, RequestContext(request))
