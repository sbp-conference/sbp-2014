from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from models import Page

# Create your views here.

def home(request, **kwargs):
    context = { 'page_title': 'SBP 2013',
                'name': 'home',
                'fonts': ''}


    return render_to_response("base/index.html", context, RequestContext(request))

def about(request, **kwargs):
    page_title = kwargs.get('page')
    stringoftext = "<div class=\"title\"><h3>Our Story</h3></div><p><i>The 2013 International Conference on Social Computing, Behavioral-Cultural Modeling, and Prediction (SBP)</i> is a multidisciplinary conference with a selective single paper track and poster session.  SBP also invites  a small number of high quality tutorials and nationally recognized keynote speakers.</p><p>The SBP conference provides a forum for researchers and practitioners from academia, industry, and government agencies to exchange ideas on current challenges in social computing, behavioral modeling and prediction, and on state-of-the-art methods and best practices being adopted to tackle these challenges. Interactive events at the conference are designed to promote cross-disciplinary contact.</p><p><b>Social Computing</b> harnesses the power of computational methods to study social behavior within a social context. <b>Behavioral Cultural  modeling</b> refers to representing behavior and culture in the abstract, and is a convenient and powerful way to conduct virtual experiments and scenario analysis. Both social computing and behavioralcultural  modeling are techniques designed to achieve a better understanding of complex behaviors, patterns, and associated outcomes of interest. Moreover, these approaches are inherently interdisciplinary; subsystems and system components exist at multiple levels of analysis (i.e., \"cells to societies\") and across multiple disciplines, from engineering and the computational sciences to the social and health sciences.</p>"
    context = { 'page_title': page_title,
                'page_contents': stringoftext,
                'fonts': ''}
    return render_to_response("base/page.html", context, RequestContext(request))

def cfp(request, **kwargs):
    context = { 'page_title': 'Call for Papers',
                'name': 'home',
                'fonts': ''}
    return render_to_response("base/cfp.html", context, RequestContext(request))

def committee(request, **kwargs):
    context = { 'page_title': 'Committee',
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
