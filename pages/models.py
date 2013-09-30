from django.db import models
from django.contrib.auth.models import User
from django.template import Library


# Create your models here.
class Page(models.Model):
    url          = models.CharField(max_length=50)
    page_title   = models.CharField(max_length=200)
    main_article = models.TextField(blank=True)
    sidebar      = models.TextField(blank=True)

    class Meta:
        ordering = ['page_title']

    def __unicode__(self):
        return u'%s %s %s' % (self.page_title, self.main_article, self.sidebar)


class Committee(models.Model):
    role        = models.CharField(max_length=50)
    full_name   = models.CharField(max_length=200)
    affiliation = models.TextField(blank=True)
    link        = models.TextField(blank=True)

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return u'%s %s %s %s' % (self.role, self.full_name, self.affiliation, self.link)
