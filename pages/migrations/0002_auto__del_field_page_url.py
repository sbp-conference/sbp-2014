# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Page.url'
        db.delete_column(u'pages_page', 'url')


    def backwards(self, orm):
        # Adding field 'Page.url'
        db.add_column(u'pages_page', 'url',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2013, 9, 30, 0, 0), max_length=50),
                      keep_default=False)


    models = {
        u'pages.page': {
            'Meta': {'ordering': "['page_title']", 'object_name': 'Page'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_article': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'page_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sidebar': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['pages']