# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):
    
    def forwards(self, orm):
        "Write your forwards methods here."
    
    
    def backwards(self, orm):
        "Write your backwards methods here."
    
    models = {
        'ged4gem.gadm_country_facts_00': {
            'Meta': {'object_name': 'gadm_country_facts_00'},
            'building_area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'built_ratio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dwellings_building': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gadm_country_alias': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gadm_country_attribute_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'gadm_country_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'gadm_country_id': ('django.db.models.fields.IntegerField', [], {}),
            'gadm_country_iso': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'gadm_country_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gadm_country_shape_area': ('django.db.models.fields.FloatField', [], {}),
            'gadm_country_shape_perimeter': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapping_schemes': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'moresimplegeom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'num_buildings': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'people_dwelling': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'populated_ratio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'population': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'population_src_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'population_src_description': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'population_src_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'population_src_source': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'replacement_cost': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'urban_rural_source': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'ged4gem.gadm_country_facts_05': {
            'Meta': {'object_name': 'gadm_country_facts_05'},
            'building_area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'built_ratio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dwellings_building': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gadm_country_alias': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gadm_country_attribute_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'gadm_country_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'gadm_country_id': ('django.db.models.fields.IntegerField', [], {}),
            'gadm_country_iso': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'gadm_country_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gadm_country_shape_area': ('django.db.models.fields.FloatField', [], {}),
            'gadm_country_shape_perimeter': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapping_schemes': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'moresimplegeom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'num_buildings': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'people_dwelling': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'populated_ratio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'population': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'population_src_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'population_src_description': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'population_src_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'population_src_source': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'replacement_cost': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'urban_rural_source': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'ged4gem.gadm_country_facts_10': {
            'Meta': {'object_name': 'gadm_country_facts_10'},
            'building_area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'built_ratio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dwellings_building': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gadm_country_alias': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gadm_country_attribute_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'gadm_country_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'gadm_country_id': ('django.db.models.fields.IntegerField', [], {}),
            'gadm_country_iso': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'gadm_country_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gadm_country_shape_area': ('django.db.models.fields.FloatField', [], {}),
            'gadm_country_shape_perimeter': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapping_schemes': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'moresimplegeom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'num_buildings': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'people_dwelling': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'populated_ratio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'population': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'population_src_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'population_src_description': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'population_src_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'population_src_source': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'replacement_cost': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'urban_rural_source': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'ged4gem.gadm_country_facts_90': {
            'Meta': {'object_name': 'gadm_country_facts_90'},
            'building_area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'built_ratio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dwellings_building': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gadm_country_alias': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gadm_country_attribute_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'gadm_country_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'gadm_country_id': ('django.db.models.fields.IntegerField', [], {}),
            'gadm_country_iso': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'gadm_country_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gadm_country_shape_area': ('django.db.models.fields.FloatField', [], {}),
            'gadm_country_shape_perimeter': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapping_schemes': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'moresimplegeom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'num_buildings': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'people_dwelling': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'populated_ratio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'population': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'population_src_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'population_src_description': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'population_src_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'population_src_source': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'replacement_cost': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'urban_rural_source': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'ged4gem.gadm_country_facts_95': {
            'Meta': {'object_name': 'gadm_country_facts_95'},
            'building_area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'built_ratio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dwellings_building': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gadm_country_alias': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gadm_country_attribute_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'gadm_country_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'gadm_country_id': ('django.db.models.fields.IntegerField', [], {}),
            'gadm_country_iso': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'gadm_country_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gadm_country_shape_area': ('django.db.models.fields.FloatField', [], {}),
            'gadm_country_shape_perimeter': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapping_schemes': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'moresimplegeom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'num_buildings': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'people_dwelling': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'populated_ratio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'population': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'population_src_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'population_src_description': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'population_src_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'population_src_source': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'replacement_cost': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'urban_rural_source': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }
    
    complete_apps = ['ged4gem']
