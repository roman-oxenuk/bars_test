# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Organization'
        db.create_table('main_organization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('inn', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('kpp', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Organization'])),
        ))
        db.send_create_signal('main', ['Organization'])

        # Adding model 'Person'
        db.create_table('main_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('patronymic', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Organization'])),
        ))
        db.send_create_signal('main', ['Person'])


    def backwards(self, orm):
        # Deleting model 'Organization'
        db.delete_table('main_organization')

        # Deleting model 'Person'
        db.delete_table('main_person')


    models = {
        'main.organization': {
            'Meta': {'object_name': 'Organization'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inn': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'kpp': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Organization']"})
        },
        'main.person': {
            'Meta': {'object_name': 'Person'},
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Organization']"}),
            'patronymic': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['main']