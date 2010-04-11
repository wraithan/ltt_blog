# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Category'
        db.create_table('yadba_category', (
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('yadba', ['Category'])

        # Adding model 'Entry'
        db.create_table('yadba_entry', (
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('tags', self.gf('tagging.fields.TagField')(default='')),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_posted', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('yadba', ['Entry'])

        # Adding M2M table for field categories on 'Entry'
        db.create_table('yadba_entry_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('entry', models.ForeignKey(orm['yadba.entry'], null=False)),
            ('category', models.ForeignKey(orm['yadba.category'], null=False))
        ))
        db.create_unique('yadba_entry_categories', ['entry_id', 'category_id'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Category'
        db.delete_table('yadba_category')

        # Deleting model 'Entry'
        db.delete_table('yadba_entry')

        # Removing M2M table for field categories on 'Entry'
        db.delete_table('yadba_entry_categories')
    
    
    models = {
        'yadba.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'yadba.entry': {
            'Meta': {'object_name': 'Entry'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['yadba.Category']", 'symmetrical': 'False'}),
            'date_posted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tags': ('tagging.fields.TagField', [], {'default': "''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }
    
    complete_apps = ['yadba']
