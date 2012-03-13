# encoding: utf-8

# Copyright (c) 2010-2012, GEM Foundation.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/agpl.html>.

import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        from django.core.management import call_command
        call_command("loaddata", "fe_fixtures.json")


    def backwards(self, orm):
        "Write your backwards methods here."


    models = {
        'observations.fault': {
            'Meta': {'object_name': 'Fault'},
            'all_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'aseis_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'aseis_slip': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'compiler': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'contrib': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '3', 'blank': 'True'}),
            'dip_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_dir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_pref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dis_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dis_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dis_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'down_thro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'episodi_ac': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'episodi_is': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'fault_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'length_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'length_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mov_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mov_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mov_pref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_pre': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'simple_geom': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {'null': 'True', 'blank': 'True'}),
            'slip_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_typ': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'strike': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'observations.faultsection': {
            'Meta': {'object_name': 'FaultSection'},
            'all_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'aseis_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'aseis_slip': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'compiler': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'contrib': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '3', 'blank': 'True'}),
            'dip_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_dir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_pref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dis_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dis_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dis_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'down_thro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'episodi_ac': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'episodi_is': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'fault': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['observations.Fault']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'length_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'length_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mov_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mov_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mov_pref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_pre': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sec_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slip_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_typ': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'strike': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'observations.faultsource': {
            'Meta': {'object_name': 'FaultSource'},
            'all_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'area_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'area_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'area_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'aseis_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'aseis_slip': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'compiler': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'contrib': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'created': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '3', 'blank': 'True'}),
            'dip_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_dir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_pref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dis_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dis_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dis_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fault': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['observations.Fault']"}),
            'geom': ('django.contrib.gis.db.models.fields.PolygonField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'length_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'length_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mag_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mag_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mag_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mom_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mom_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mom_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mov_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mov_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mov_pref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_pre': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slip_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_typ': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'fault_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'u_sm_d_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'width_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'width_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'width_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'observations.observations': {
            'Meta': {'object_name': 'Observations'},
            'dip_slip_rate_max': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'dip_slip_rate_min': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'dip_slip_rate_pref': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'hv_ratio': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marker_age': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'net_slip_rate_max': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'net_slip_rate_min': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'net_slip_rate_pref': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'observationType': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'rake': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'slipType': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'slip_rate_category': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'strike_slip_rate_max': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'strike_slip_rate_min': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'strike_slip_rate_pref': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'summary_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'vertical_slip_rate_max': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'vertical_slip_rate_min': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'vertical_slip_rate_pref': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'observations.siteobservation': {
            'Meta': {'object_name': 'SiteObservation'},
            'accuracy': ('django.db.models.fields.BigIntegerField', [], {}),
            'fault_section': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['observations.FaultSection']", 'symmetrical': 'False'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            's_feature': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'scale': ('django.db.models.fields.BigIntegerField', [], {})
        },
        'observations.trace': {
            'Meta': {'object_name': 'Trace'},
            'accuracy': ('django.db.models.fields.BigIntegerField', [], {}),
            'fault_section': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['observations.FaultSection']", 'symmetrical': 'False'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loc_meth': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'scale': ('django.db.models.fields.BigIntegerField', [], {}),
            'tid': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['observations']
