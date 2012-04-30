# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Geodetic'
        db.create_table('geodetic_geodetic', (
            ('gid', self.gf('django.db.models.fields.IntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('lon', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('exx', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('eyy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('exy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('var_exx', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('var_exy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('var_eyy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('cc_xx_yy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('cc_xx_xy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('cc_yy_xy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('x_azimuth', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('exx_psr', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('eyy_psr', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('the_geom', self.gf('django.contrib.gis.db.models.fields.PointField')(dim=2)),
            ))
        db.send_create_signal('geodetic', ['Geodetic'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Geodetic'
        db.delete_table('geodetic_geodetic')
    
    
    models = {
        'geodetic.geodetic': {
            'Meta': {'object_name': 'Geodetic'},
            'gid': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lon': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'exx': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'eyy': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'exy': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'var_exx': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'var_eyy': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'var_exy': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cc_xx_yy': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cc_xx_xy': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cc_yy_xy': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'x_azimuth': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'exx_psr': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'eyy_psr': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'the_geom': ('django.contrib.gis.db.models.fields.PointField', [], {'dim': '2'})
        }
    }
    
    complete_apps = ['geodetic']
