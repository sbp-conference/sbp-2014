# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Page'
        db.create_table(u'pages_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('page_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('main_article', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('sidebar', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'pages', ['Page'])


    def backwards(self, orm):
        # Deleting model 'Page'
        db.delete_table(u'pages_page')


    models = {
        u'pages.page': {
            'Meta': {'ordering': "['page_title']", 'object_name': 'Page'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_article': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'page_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sidebar': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['pages']