# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'gadm_country_facts'
        db.create_table('ged4gem_gadm_country_facts', (
            ('building_area', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('populated_ratio', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('moresimplegeom', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gedid', self.gf('django.db.models.fields.IntegerField')()),
            ('people_dwelling', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('num_buildings', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('gadm_country_id', self.gf('django.db.models.fields.IntegerField')()),
            ('urban_rural_source', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('population_src_description', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('population_src_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('gadm_country_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('mapping_schemes', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('population_src_source', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('gadm_country_iso', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('population', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('replacement_cost', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('population_src_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('gadm_country_alias', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('gadm_country_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('built_ratio', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('gadm_country_shape_perimeter', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('gadm_country_attribute_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('gadm_country_shape_area', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('dwellings_building', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('ged4gem', ['gadm_country_facts'])

        # Adding model 'gadm_country_facts_00'
        db.create_table('ged4gem_gadm_country_facts_00', (
            ('building_area', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('populated_ratio', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('moresimplegeom', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gedid', self.gf('django.db.models.fields.IntegerField')()),
            ('people_dwelling', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('num_buildings', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('gadm_country_id', self.gf('django.db.models.fields.IntegerField')()),
            ('urban_rural_source', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('population_src_description', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('population_src_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('gadm_country_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('mapping_schemes', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('population_src_source', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('gadm_country_iso', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('population', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('replacement_cost', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('population_src_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('gadm_country_alias', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('gadm_country_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('built_ratio', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('gadm_country_shape_perimeter', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('gadm_country_attribute_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('gadm_country_shape_area', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('dwellings_building', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('ged4gem', ['gadm_country_facts_00'])

        # Adding model 'gadm_country_facts_05'
        db.create_table('ged4gem_gadm_country_facts_05', (
            ('building_area', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('populated_ratio', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('moresimplegeom', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gedid', self.gf('django.db.models.fields.IntegerField')()),
            ('people_dwelling', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('num_buildings', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('gadm_country_id', self.gf('django.db.models.fields.IntegerField')()),
            ('urban_rural_source', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('population_src_description', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('population_src_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('gadm_country_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('mapping_schemes', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('population_src_source', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('gadm_country_iso', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('population', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('replacement_cost', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('population_src_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('gadm_country_alias', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('gadm_country_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('built_ratio', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('gadm_country_shape_perimeter', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('gadm_country_attribute_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('gadm_country_shape_area', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('dwellings_building', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('ged4gem', ['gadm_country_facts_05'])

        # Adding model 'gadm_country_facts_10'
        db.create_table('ged4gem_gadm_country_facts_10', (
            ('building_area', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('populated_ratio', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('moresimplegeom', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gedid', self.gf('django.db.models.fields.IntegerField')()),
            ('people_dwelling', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('num_buildings', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('gadm_country_id', self.gf('django.db.models.fields.IntegerField')()),
            ('urban_rural_source', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('population_src_description', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('population_src_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('gadm_country_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('mapping_schemes', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('population_src_source', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('gadm_country_iso', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('population', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('replacement_cost', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('population_src_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('gadm_country_alias', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('gadm_country_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('built_ratio', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('gadm_country_shape_perimeter', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('gadm_country_attribute_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('gadm_country_shape_area', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('dwellings_building', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('ged4gem', ['gadm_country_facts_10'])

        # Adding model 'gadm_country_facts_90'
        db.create_table('ged4gem_gadm_country_facts_90', (
            ('building_area', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('populated_ratio', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('moresimplegeom', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gedid', self.gf('django.db.models.fields.IntegerField')()),
            ('people_dwelling', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('num_buildings', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('gadm_country_id', self.gf('django.db.models.fields.IntegerField')()),
            ('urban_rural_source', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('population_src_description', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('population_src_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('gadm_country_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('mapping_schemes', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('population_src_source', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('gadm_country_iso', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('population', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('replacement_cost', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('population_src_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('gadm_country_alias', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('gadm_country_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('built_ratio', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('gadm_country_shape_perimeter', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('gadm_country_attribute_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('gadm_country_shape_area', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('dwellings_building', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('ged4gem', ['gadm_country_facts_90'])

        # Adding model 'gadm_country_facts_95'
        db.create_table('ged4gem_gadm_country_facts_95', (
            ('building_area', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('populated_ratio', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('moresimplegeom', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gedid', self.gf('django.db.models.fields.IntegerField')()),
            ('people_dwelling', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('num_buildings', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('gadm_country_id', self.gf('django.db.models.fields.IntegerField')()),
            ('urban_rural_source', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('population_src_description', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('population_src_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('gadm_country_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('mapping_schemes', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('population_src_source', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('gadm_country_iso', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('population', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('replacement_cost', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('population_src_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('gadm_country_alias', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('gadm_country_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('built_ratio', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('gadm_country_shape_perimeter', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('gadm_country_attribute_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('gadm_country_shape_area', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('dwellings_building', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('ged4gem', ['gadm_country_facts_95'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'gadm_country_facts'
        db.delete_table('ged4gem_gadm_country_facts')

        # Deleting model 'gadm_country_facts_00'
        db.delete_table('ged4gem_gadm_country_facts_00')

        # Deleting model 'gadm_country_facts_05'
        db.delete_table('ged4gem_gadm_country_facts_05')

        # Deleting model 'gadm_country_facts_10'
        db.delete_table('ged4gem_gadm_country_facts_10')

        # Deleting model 'gadm_country_facts_90'
        db.delete_table('ged4gem_gadm_country_facts_90')

        # Deleting model 'gadm_country_facts_95'
        db.delete_table('ged4gem_gadm_country_facts_95')
    
    
    models = {
        'ged4gem.gadm_country_facts': {
            'Meta': {'object_name': 'gadm_country_facts'},
            'building_area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'built_ratio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dwellings_building': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gadm_country_alias': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gadm_country_attribute_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'gadm_country_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'gadm_country_id': ('django.db.models.fields.IntegerField', [], {}),
            'gadm_country_iso': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'gadm_country_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gadm_country_shape_area': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'gadm_country_shape_perimeter': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'gedid': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapping_schemes': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'moresimplegeom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
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
            'gadm_country_shape_area': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'gadm_country_shape_perimeter': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'gedid': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapping_schemes': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'moresimplegeom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
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
            'gadm_country_shape_area': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'gadm_country_shape_perimeter': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'gedid': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapping_schemes': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'moresimplegeom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
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
            'gadm_country_shape_area': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'gadm_country_shape_perimeter': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'gedid': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapping_schemes': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'moresimplegeom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
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
            'gadm_country_shape_area': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'gadm_country_shape_perimeter': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'gedid': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapping_schemes': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'moresimplegeom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
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
            'gadm_country_shape_area': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'gadm_country_shape_perimeter': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'gedid': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapping_schemes': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'moresimplegeom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
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
