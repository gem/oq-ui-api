# encoding: utf-8

#Copyright (C) 2012  FaultedEarth
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
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):

        # fault section view
        db.execute("""CREATE VIEW gem.fault_section_view AS
SELECT
    observations_faultsection.id, observations_faultsection.sec_name,
    observations_faultsection.length_min, observations_faultsection.length_max,
    observations_faultsection.length_pre, observations_faultsection.strike,
    observations_faultsection.episodi_is, observations_faultsection.episodi_ac,
    observations_faultsection.u_sm_d_min, observations_faultsection.u_sm_d_max,
    observations_faultsection.u_sm_d_pre, observations_faultsection.u_sm_d_com,
    observations_faultsection.low_d_min, observations_faultsection.low_d_max,
    observations_faultsection.low_d_pref, observations_faultsection.low_d_com,
    observations_faultsection.dip_min, observations_faultsection.dip_max,
    observations_faultsection.dip_pref, observations_faultsection.dip_com,
    observations_faultsection.dip_dir, observations_faultsection.down_thro,
    observations_faultsection.slip_typ, observations_faultsection.slip_com,
    observations_faultsection.slip_r_min, observations_faultsection.slip_r_max,
    observations_faultsection.slip_r_pre, observations_faultsection.slip_r_com,
    observations_faultsection.aseis_slip, observations_faultsection.aseis_com,
    observations_faultsection.dis_min, observations_faultsection.dis_max,
    observations_faultsection.dis_pref, observations_faultsection.re_int_min,
    observations_faultsection.re_int_max, observations_faultsection.re_int_pre,
    observations_faultsection.mov_min,
    observations_faultsection.mov_max, observations_faultsection.mov_pref,
    observations_faultsection.all_com, observations_faultsection.compiler,
    observations_faultsection.contrib, observations_faultsection.created,
    ST_Multi(ST_Union(observations_trace.geom)) as geom
FROM gem.observations_faultsection
JOIN gem.observations_trace_fault_section ON observations_faultsection.id = observations_trace_fault_section.faultsection_id
JOIN gem.observations_trace ON observations_trace_fault_section.trace_id = observations_trace.id
GROUP BY
    observations_faultsection.id, observations_faultsection.sec_name,
    observations_faultsection.length_min, observations_faultsection.length_max,
    observations_faultsection.length_pre, observations_faultsection.strike,
    observations_faultsection.episodi_is, observations_faultsection.episodi_ac,
    observations_faultsection.u_sm_d_min, observations_faultsection.u_sm_d_max,
    observations_faultsection.u_sm_d_pre, observations_faultsection.u_sm_d_com,
    observations_faultsection.low_d_min, observations_faultsection.low_d_max,
    observations_faultsection.low_d_pref, observations_faultsection.low_d_com,
    observations_faultsection.dip_min, observations_faultsection.dip_max,
    observations_faultsection.dip_pref, observations_faultsection.dip_com,
    observations_faultsection.dip_dir, observations_faultsection.down_thro,
    observations_faultsection.slip_typ, observations_faultsection.slip_com,
    observations_faultsection.slip_r_min, observations_faultsection.slip_r_max,
    observations_faultsection.slip_r_pre, observations_faultsection.slip_r_com,
    observations_faultsection.aseis_slip, observations_faultsection.aseis_com,
    observations_faultsection.dis_min, observations_faultsection.dis_max,
    observations_faultsection.dis_pref, observations_faultsection.re_int_min,
    observations_faultsection.re_int_max, observations_faultsection.re_int_pre,
    observations_faultsection.mov_min,
    observations_faultsection.mov_max, observations_faultsection.mov_pref,
    observations_faultsection.all_com, observations_faultsection.compiler,
    observations_faultsection.contrib, observations_faultsection.created;
""")

        # fault section view update rule
        db.execute("""
CREATE RULE
    fault_section_view_update
AS ON UPDATE TO
    gem.fault_section_view
DO INSTEAD
UPDATE
    gem.observations_faultsection
SET
    sec_name = NEW.sec_name,
    length_min = NEW.length_min, length_max = NEW.length_max,
    length_pre = NEW.length_pre, strike = NEW.strike,
    episodi_is = NEW.episodi_is, episodi_ac = NEW.episodi_ac,
    u_sm_d_min = NEW.u_sm_d_min, u_sm_d_max = NEW.u_sm_d_max,
    u_sm_d_pre = NEW.u_sm_d_pre, u_sm_d_com = NEW.u_sm_d_com,
    low_d_min = NEW.low_d_min, low_d_max = NEW.low_d_max,
    low_d_pref = NEW.low_d_pref, low_d_com = NEW.low_d_com,
    dip_min = NEW.dip_min, dip_max = NEW.dip_max,
    dip_pref = NEW.dip_pref, dip_com = NEW.dip_com,
    dip_dir = NEW.dip_dir, down_thro = NEW.down_thro,
    slip_typ = NEW.slip_typ, slip_com = NEW.slip_com,
    slip_r_min = NEW.slip_r_min, slip_r_max = NEW.slip_r_max,
    slip_r_pre = NEW.slip_r_pre, slip_r_com = NEW.slip_r_com,
    aseis_slip = NEW.aseis_slip, aseis_com = NEW.aseis_com,
    dis_min = NEW.dis_min, dis_max = NEW.dis_max,
    dis_pref = NEW.dis_pref, re_int_min = NEW.re_int_min,
    re_int_max = NEW.re_int_max, re_int_pre = NEW.re_int_pre,
    mov_min = NEW.mov_min,
    mov_max = NEW.mov_max, mov_pref = NEW.mov_pref,
    all_com = NEW.all_com, compiler = NEW.compiler,
    contrib = NEW.contrib, created = NEW.created
WHERE
    id = OLD.id;
""")

        # fault view
        db.execute("""CREATE VIEW gem.fault_view AS
                SELECT observations_fault.id,
        observations_fault.fault_name, observations_fault.length_min,
        observations_fault.length_max, observations_fault.length_pre,
        observations_fault.strike, observations_fault.episodi_is,
        observations_fault.episodi_ac, observations_fault.u_sm_d_min,
        observations_fault.u_sm_d_max, observations_fault.u_sm_d_pre,
        observations_fault.u_sm_d_com, observations_fault.low_d_min,
        observations_fault.low_d_max, observations_fault.low_d_pref,
        observations_fault.low_d_com, observations_fault.dip_min,
        observations_fault.dip_max, observations_fault.dip_pref,
        observations_fault.dip_com, observations_fault.dip_dir,
        observations_fault.down_thro, observations_fault.slip_typ,
        observations_fault.slip_com, observations_fault.slip_r_min,
        observations_fault.slip_r_max, observations_fault.slip_r_pre,
        observations_fault.slip_r_com, observations_fault.aseis_slip,
        observations_fault.aseis_com, observations_fault.dis_min,
        observations_fault.dis_max, observations_fault.dis_pref,
        observations_fault.re_int_min, observations_fault.re_int_max,
        observations_fault.re_int_pre, observations_fault.mov_min,
        observations_fault.mov_max, observations_fault.mov_pref,
        observations_fault.all_com, observations_fault.compiler,
        observations_fault.contrib, observations_fault.created,
        St_Multi(St_Union(observations_trace.geom)) as geom
FROM gem.observations_fault
JOIN gem.observations_faultsection_fault ON
observations_fault.id = observations_faultsection_fault.fault_id
JOIN gem.observations_faultsection ON observations_faultsection.id =
observations_faultsection_fault.faultsection_id
JOIN gem.observations_trace_fault_section ON gem.observations_faultsection.id = observations_trace_fault_section.faultsection_id
JOIN gem.observations_trace ON gem.observations_trace.id = observations_trace_fault_section.trace_id
GROUP BY
        observations_fault.id,
        observations_fault.fault_name, observations_fault.length_min,
        observations_fault.length_max, observations_fault.length_pre,
        observations_fault.strike, observations_fault.episodi_is,
        observations_fault.episodi_ac, observations_fault.u_sm_d_min,
        observations_fault.u_sm_d_max, observations_fault.u_sm_d_pre,
        observations_fault.u_sm_d_com, observations_fault.low_d_min,
        observations_fault.low_d_max, observations_fault.low_d_pref,
        observations_fault.low_d_com, observations_fault.dip_min,
        observations_fault.dip_max, observations_fault.dip_pref,
        observations_fault.dip_com, observations_fault.dip_dir,
        observations_fault.down_thro, observations_fault.slip_typ,
        observations_fault.slip_com, observations_fault.slip_r_min,
        observations_fault.slip_r_max, observations_fault.slip_r_pre,
        observations_fault.slip_r_com, observations_fault.aseis_slip,
        observations_fault.aseis_com, observations_fault.dis_min,
        observations_fault.dis_max, observations_fault.dis_pref,
        observations_fault.re_int_min, observations_fault.re_int_max,
        observations_fault.re_int_pre, observations_fault.mov_min,
        observations_fault.mov_max, observations_fault.mov_pref,
        observations_fault.all_com, observations_fault.compiler,
        observations_fault.contrib, observations_fault.created""")

        # fault view update rule
        db.execute("""
CREATE RULE
    fault_view_update
AS ON UPDATE TO
    gem.fault_view
DO INSTEAD
UPDATE
    gem.observations_fault
SET
    fault_name = NEW.fault_name, length_min = NEW.length_min,
    length_max = NEW.length_max, length_pre = NEW.length_pre,
    strike = NEW.strike, episodi_is = NEW.episodi_is,
    episodi_ac = NEW.episodi_ac, u_sm_d_min = NEW.u_sm_d_min,
    u_sm_d_max = NEW.u_sm_d_max, u_sm_d_pre = NEW.u_sm_d_pre,
    u_sm_d_com = NEW.u_sm_d_com, low_d_min = NEW.low_d_min,
    low_d_max = NEW.low_d_max, low_d_pref = NEW.low_d_pref,
    low_d_com = NEW.low_d_com, dip_min = NEW.dip_min,
    dip_max = NEW.dip_max, dip_pref = NEW.dip_pref,
    dip_com = NEW.dip_com, dip_dir = NEW.dip_dir,
    down_thro = NEW.down_thro, slip_typ = NEW.slip_typ,
    slip_com = NEW.slip_com, slip_r_min = NEW.slip_r_min,
    slip_r_max = NEW.slip_r_max, slip_r_pre = NEW.slip_r_pre,
    slip_r_com = NEW.slip_r_com, aseis_slip = NEW.aseis_slip,
    aseis_com = NEW.aseis_com, dis_min = NEW.dis_min,
    dis_max = NEW.dis_max, dis_pref = NEW.dis_pref,
    re_int_min = NEW.re_int_min, re_int_max = NEW.re_int_max,
    re_int_pre = NEW.re_int_pre, mov_min = NEW.mov_min,
    mov_max = NEW.mov_max, mov_pref = NEW.mov_pref,
    all_com = NEW.all_com, compiler = NEW.compiler,
    contrib = NEW.contrib, created = NEW.created
WHERE
    id = OLD.id;
        """)
        
        # folds
        
        # fold section view
        db.execute("""CREATE VIEW gem.fold_section_view AS
SELECT
    observations_foldsection.id, observations_foldsection.sec_name,
    observations_foldsection.length_min, observations_foldsection.length_max,
    observations_foldsection.length_pre,
    observations_foldsection.episodi_is, observations_foldsection.episodi_ac,
    observations_foldsection.fold_type, observations_foldsection.symmetry,
    observations_foldsection.asymm_dir, observations_foldsection.dip_axial,
    observations_foldsection.dip_limbs, observations_foldsection.plunge,
    observations_foldsection.tilt_rate, observations_foldsection.growth_vert,
    observations_foldsection.growth_hori, observations_foldsection.surf_age,
    observations_foldsection.mov_min,
    observations_foldsection.mov_max, observations_foldsection.mov_pref,
    observations_foldsection.all_com, observations_foldsection.compiler,
    observations_foldsection.contrib, observations_foldsection.created,
    ST_Multi(ST_Union(observations_foldtrace.geom)) as geom
FROM gem.observations_foldsection
JOIN gem.observations_foldtrace_fold_section ON observations_foldsection.id = observations_foldtrace_fold_section.foldsection_id
JOIN gem.observations_foldtrace ON observations_foldtrace_fold_section.foldtrace_id = observations_foldtrace.id
GROUP BY
    observations_foldsection.id, observations_foldsection.sec_name,
    observations_foldsection.length_min, observations_foldsection.length_max,
    observations_foldsection.length_pre,
    observations_foldsection.episodi_is, observations_foldsection.episodi_ac,
    observations_foldsection.fold_type, observations_foldsection.symmetry,
    observations_foldsection.asymm_dir, observations_foldsection.dip_axial,
    observations_foldsection.dip_limbs, observations_foldsection.plunge,
    observations_foldsection.tilt_rate, observations_foldsection.growth_vert,
    observations_foldsection.growth_hori, observations_foldsection.surf_age,
    observations_foldsection.mov_min,
    observations_foldsection.mov_max, observations_foldsection.mov_pref,
    observations_foldsection.all_com, observations_foldsection.compiler,
    observations_foldsection.contrib, observations_foldsection.created;
""")
        # fold section view update rule
        db.execute("""
CREATE RULE
    fold_section_view_update
AS ON UPDATE TO
    gem.fold_section_view
DO INSTEAD
UPDATE
    gem.observations_foldsection
SET
    sec_name = NEW.sec_name,
    length_min = NEW.length_min, length_max = NEW.length_max,
    length_pre = NEW.length_pre,
    episodi_is = NEW.episodi_is, episodi_ac = NEW.episodi_ac,
    fold_type = NEW.fold_type, symmetry = NEW.symmetry,
    asymm_dir = NEW.asymm_dir, dip_axial = NEW.dip_axial,
    dip_limbs = NEW.dip_limbs, plunge = NEW.plunge,
    tilt_rate = NEW.tilt_rate, growth_vert = NEW.growth_vert,
    growth_hori = NEW.growth_hori, surf_age = NEW.surf_age,
    mov_min = NEW.mov_min,
    mov_max = NEW.mov_max, mov_pref = NEW.mov_pref,
    all_com = NEW.all_com, compiler = NEW.compiler,
    contrib = NEW.contrib, created = NEW.created
WHERE
    id = OLD.id;
""")

        # fold view
        db.execute("""CREATE VIEW gem.fold_view AS
SELECT observations_fold.id, observations_fold.aseis_slip,
    observations_fold.fold_name, observations_fold.length_min,
    observations_fold.length_max, observations_fold.length_pre,
    observations_fold.strike, observations_fold.episodi_is,
    observations_fold.episodi_ac, observations_fold.u_sm_d_min,
    observations_fold.u_sm_d_max, observations_fold.u_sm_d_pre,
    observations_fold.u_sm_d_com, observations_fold.low_d_min,
    observations_fold.low_d_max, observations_fold.low_d_pref,
    observations_fold.low_d_com, observations_fold.dip_min,
    observations_fold.dip_max, observations_fold.dip_pref,
    observations_fold.dip_com, observations_fold.dip_dir,
    observations_fold.asymm_dir, observations_fold.slip_typ,
    observations_fold.fold_type, observations_fold.symmetry,
    observations_fold.slip_com, observations_fold.slip_r_min,
    observations_fold.slip_r_max, observations_fold.slip_r_pre,
    observations_fold.slip_r_com, observations_fold.re_int_min,
    observations_fold.re_int_max, observations_fold.re_int_pre,
    observations_fold.all_com, observations_fold.compiler,
    observations_fold.contrib, observations_fold.created,
    St_Multi(St_Union(observations_foldtrace.geom)) as geom
FROM gem.observations_fold
JOIN gem.observations_foldsection_fold ON
observations_fold.id = observations_foldsection_fold.fold_id
JOIN gem.observations_foldsection ON observations_foldsection.id =
observations_foldsection_fold.foldsection_id
JOIN gem.observations_foldtrace_fold_section ON gem.observations_foldsection.id = observations_foldtrace_fold_section.foldsection_id
JOIN gem.observations_foldtrace ON gem.observations_foldtrace.id = observations_foldtrace_fold_section.foldtrace_id
GROUP BY
    observations_fold.id, observations_fold.aseis_slip,
        observations_fold.fold_name, observations_fold.length_min,
        observations_fold.length_max, observations_fold.length_pre,
        observations_fold.strike, observations_fold.episodi_is,
        observations_fold.episodi_ac, observations_fold.u_sm_d_min,
        observations_fold.u_sm_d_max, observations_fold.u_sm_d_pre,
        observations_fold.u_sm_d_com, observations_fold.low_d_min,
        observations_fold.low_d_max, observations_fold.low_d_pref,
        observations_fold.low_d_com, observations_fold.dip_min,
        observations_fold.dip_max, observations_fold.dip_pref,
        observations_fold.dip_com, observations_fold.dip_dir,
        observations_fold.asymm_dir, observations_fold.slip_typ,
        observations_fold.fold_type, observations_fold.symmetry,
        observations_fold.slip_com, observations_fold.slip_r_min,
        observations_fold.slip_r_max, observations_fold.slip_r_pre,
        observations_fold.slip_r_com, observations_fold.re_int_min,
        observations_fold.re_int_max, observations_fold.re_int_pre,
        observations_fold.all_com, observations_fold.compiler,
        observations_fold.contrib, observations_fold.created""")
        
        # fold view update rule
        db.execute("""
CREATE RULE
    fold_view_update
AS ON UPDATE TO
    gem.fold_view
DO INSTEAD
UPDATE
    gem.observations_fold
SET
    fold_name = NEW.fold_name, length_min = NEW.length_min,
    length_max = NEW.length_max, length_pre = NEW.length_pre,
    strike = NEW.strike, episodi_is = NEW.episodi_is,
    episodi_ac = NEW.episodi_ac, u_sm_d_min = NEW.u_sm_d_min,
    u_sm_d_max = NEW.u_sm_d_max, u_sm_d_pre = NEW.u_sm_d_pre,
    u_sm_d_com = NEW.u_sm_d_com, low_d_min = NEW.low_d_min,
    low_d_max = NEW.low_d_max, low_d_pref = NEW.low_d_pref,
    low_d_com = NEW.low_d_com, dip_min = NEW.dip_min,
    dip_max = NEW.dip_max, dip_pref = NEW.dip_pref,
    dip_com = NEW.dip_com, dip_dir = NEW.dip_dir,
    fold_type = NEW.fold_type, symmetry = NEW.symmetry,
    asymm_dir = NEW.asymm_dir, slip_typ = NEW.slip_typ,
    slip_com = NEW.slip_com, slip_r_min = NEW.slip_r_min,
    slip_r_max = NEW.slip_r_max, slip_r_pre = NEW.slip_r_pre,
    slip_r_com = NEW.slip_r_com, aseis_slip = NEW.aseis_slip, 
    re_int_min = NEW.re_int_min, 
    re_int_max = NEW.re_int_max, re_int_pre = NEW.re_int_pre, 
    all_com = NEW.all_com, compiler = NEW.compiler,
    contrib = NEW.contrib, created = NEW.created
WHERE
    id = OLD.id;
        """)
    
        # simple geometry view

        db.execute("""CREATE VIEW gem.simple_geom_view AS
                 SELECT f.id, f.fault_name, f.simple_geom
                 FROM gem.observations_fault f""")
        
         # fold simple geometry view

        db.execute("""CREATE VIEW gem.simple_fold_geom_view AS
                  SELECT g.id, g.fold_name, g.simple_fold_geom
                  FROM gem.observations_fold g""")

        # "publish" the geometries into public.geometry_columns
        db.execute("""INSERT INTO public.geometry_columns VALUES ('', 'gem',
                'fault_section_view', 'geom', '2', 4326, 'MULTILINESTRING')""")

        db.execute("""INSERT INTO public.geometry_columns VALUES ('', 'gem',
        'fault_view', 'geom', 2, 4326, 'MULTILINESTRING')""")
        
        db.execute("""INSERT INTO public.geometry_columns VALUES ('', 'gem',
        'fold_view', 'geom', 2, 4326, 'MULTILINESTRING')""")
        
        db.execute("""INSERT INTO public.geometry_columns VALUES ('', 'gem',
        'fold_section_view', 'geom', 2, 4326, 'MULTILINESTRING')""")

        db.execute("""INSERT INTO public.geometry_columns VALUES ('', 'gem',
                'simple_geom_view', 'simple_geom', '2', 4326,
                'MULTILINESTRING')""")
                
        db.execute("""INSERT INTO public.geometry_columns VALUES ('', 'gem',
                'simple_fold_geom_view', 'simple_fold_geom', '2', 4326,
                'MULTILINESTRING')""")


    def backwards(self, orm):
        db.execute("DROP VIEW fault_section_view")
        db.execute("DROP VIEW fault_view")
        db.execute("DROP VIEW simple_geom_view")
        db.execute("DROP VIEW fold_section_view")
        db.execute("DROP VIEW fold_view")
        db.execute("DROP VIEW simple_fold_geom_view")


    models = {
        'observations.fault': {
            'Meta': {'object_name': 'Fault'},
            'all_com': ('django.db.models.fields.IntegerField', [], {}),
            'aseis_com': ('django.db.models.fields.IntegerField', [], {}),
            'aseis_slip': ('django.db.models.fields.FloatField', [], {}),
            'compiler': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'contrib': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'created': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
            'dip_com': ('django.db.models.fields.IntegerField', [], {}),
            'dip_dir': ('django.db.models.fields.IntegerField', [], {}),
            'dip_max': ('django.db.models.fields.IntegerField', [], {}),
            'dip_min': ('django.db.models.fields.IntegerField', [], {}),
            'dip_pref': ('django.db.models.fields.IntegerField', [], {}),
            'dis_max': ('django.db.models.fields.FloatField', [], {}),
            'dis_min': ('django.db.models.fields.FloatField', [], {}),
            'dis_pref': ('django.db.models.fields.FloatField', [], {}),
            'down_thro': ('django.db.models.fields.IntegerField', [], {}),
            'episodi_ac': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'episodi_is': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'fault_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_max': ('django.db.models.fields.FloatField', [], {}),
            'length_min': ('django.db.models.fields.FloatField', [], {}),
            'length_pre': ('django.db.models.fields.FloatField', [], {}),
            'low_d_com': ('django.db.models.fields.FloatField', [], {}),
            'low_d_max': ('django.db.models.fields.FloatField', [], {}),
            'low_d_min': ('django.db.models.fields.FloatField', [], {}),
            'low_d_pref': ('django.db.models.fields.FloatField', [], {}),
            'mov_max': ('django.db.models.fields.IntegerField', [], {}),
            'mov_min': ('django.db.models.fields.IntegerField', [], {}),
            'mov_pref': ('django.db.models.fields.IntegerField', [], {}),
            're_int_max': ('django.db.models.fields.IntegerField', [], {}),
            're_int_min': ('django.db.models.fields.IntegerField', [], {}),
            're_int_pre': ('django.db.models.fields.IntegerField', [], {}),
            'slip_com': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_com': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_max': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_min': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_pre': ('django.db.models.fields.IntegerField', [], {}),
            'slip_typ': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'strike': ('django.db.models.fields.IntegerField', [], {}),
            'u_sm_d_com': ('django.db.models.fields.FloatField', [], {}),
            'u_sm_d_max': ('django.db.models.fields.FloatField', [], {}),
            'u_sm_d_min': ('django.db.models.fields.FloatField', [], {}),
            'u_sm_d_pre': ('django.db.models.fields.FloatField', [], {})
        },
        'observations.faultsection': {
            'Meta': {'object_name': 'FaultSection'},
            'all_com': ('django.db.models.fields.IntegerField', [], {}),
            'aseis_com': ('django.db.models.fields.IntegerField', [], {}),
            'aseis_slip': ('django.db.models.fields.FloatField', [], {}),
            'compiler': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'contrib': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'created': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
            'dip_com': ('django.db.models.fields.IntegerField', [], {}),
            'dip_dir': ('django.db.models.fields.IntegerField', [], {}),
            'dip_max': ('django.db.models.fields.IntegerField', [], {}),
            'dip_min': ('django.db.models.fields.IntegerField', [], {}),
            'dip_pref': ('django.db.models.fields.IntegerField', [], {}),
            'dis_max': ('django.db.models.fields.FloatField', [], {}),
            'dis_min': ('django.db.models.fields.FloatField', [], {}),
            'dis_pref': ('django.db.models.fields.FloatField', [], {}),
            'down_thro': ('django.db.models.fields.IntegerField', [], {}),
            'episodi_ac': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'episodi_is': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'fault': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['observations.Fault']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_max': ('django.db.models.fields.FloatField', [], {}),
            'length_min': ('django.db.models.fields.FloatField', [], {}),
            'length_pre': ('django.db.models.fields.FloatField', [], {}),
            'low_d_com': ('django.db.models.fields.FloatField', [], {}),
            'low_d_max': ('django.db.models.fields.FloatField', [], {}),
            'low_d_min': ('django.db.models.fields.FloatField', [], {}),
            'low_d_pref': ('django.db.models.fields.FloatField', [], {}),
            'mov_max': ('django.db.models.fields.IntegerField', [], {}),
            'mov_min': ('django.db.models.fields.IntegerField', [], {}),
            'mov_pref': ('django.db.models.fields.IntegerField', [], {}),
            're_int_max': ('django.db.models.fields.IntegerField', [], {}),
            're_int_min': ('django.db.models.fields.IntegerField', [], {}),
            're_int_pre': ('django.db.models.fields.IntegerField', [], {}),
            'sec_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'slip_com': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_com': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_max': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_min': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_pre': ('django.db.models.fields.IntegerField', [], {}),
            'slip_typ': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'strike': ('django.db.models.fields.IntegerField', [], {}),
            'u_sm_d_com': ('django.db.models.fields.FloatField', [], {}),
            'u_sm_d_max': ('django.db.models.fields.FloatField', [], {}),
            'u_sm_d_min': ('django.db.models.fields.FloatField', [], {}),
            'u_sm_d_pre': ('django.db.models.fields.FloatField', [], {})
        },
        'observations.faultsource': {
            'Meta': {'object_name': 'FaultSource'},
            'all_com': ('django.db.models.fields.IntegerField', [], {}),
            'area': ('django.db.models.fields.FloatField', [], {}),
            'aseis_com': ('django.db.models.fields.IntegerField', [], {}),
            'aseis_slip': ('django.db.models.fields.FloatField', [], {}),
            'compiler': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'contrib': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'created': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
            'dip_com': ('django.db.models.fields.IntegerField', [], {}),
            'dip_dir': ('django.db.models.fields.IntegerField', [], {}),
            'dip_max': ('django.db.models.fields.IntegerField', [], {}),
            'dip_min': ('django.db.models.fields.IntegerField', [], {}),
            'dip_pref': ('django.db.models.fields.IntegerField', [], {}),
            'dis_max': ('django.db.models.fields.FloatField', [], {}),
            'dis_min': ('django.db.models.fields.FloatField', [], {}),
            'dis_pref': ('django.db.models.fields.FloatField', [], {}),
            'geom': ('django.contrib.gis.db.models.fields.PolygonField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_max': ('django.db.models.fields.FloatField', [], {}),
            'length_min': ('django.db.models.fields.FloatField', [], {}),
            'length_pre': ('django.db.models.fields.FloatField', [], {}),
            'low_d_com': ('django.db.models.fields.FloatField', [], {}),
            'low_d_max': ('django.db.models.fields.FloatField', [], {}),
            'low_d_min': ('django.db.models.fields.FloatField', [], {}),
            'low_d_pref': ('django.db.models.fields.FloatField', [], {}),
            'magnitude': ('django.db.models.fields.IntegerField', [], {}),
            'mov_max': ('django.db.models.fields.IntegerField', [], {}),
            'mov_min': ('django.db.models.fields.IntegerField', [], {}),
            'mov_pref': ('django.db.models.fields.IntegerField', [], {}),
            'rake_com': ('django.db.models.fields.IntegerField', [], {}),
            'rake_max': ('django.db.models.fields.IntegerField', [], {}),
            'rake_min': ('django.db.models.fields.IntegerField', [], {}),
            'rake_pref': ('django.db.models.fields.IntegerField', [], {}),
            're_int_max': ('django.db.models.fields.IntegerField', [], {}),
            're_int_min': ('django.db.models.fields.IntegerField', [], {}),
            're_int_pre': ('django.db.models.fields.IntegerField', [], {}),
            'slip_com': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_com': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_max': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_min': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_pre': ('django.db.models.fields.IntegerField', [], {}),
            'slip_typ': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'source_nm': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'u_sm_d_com': ('django.db.models.fields.FloatField', [], {}),
            'u_sm_d_max': ('django.db.models.fields.FloatField', [], {}),
            'u_sm_d_min': ('django.db.models.fields.FloatField', [], {}),
            'u_sm_d_pre': ('django.db.models.fields.FloatField', [], {}),
            'width': ('django.db.models.fields.FloatField', [], {})
        },
        'observations.faultsourcetrace': {
            'Meta': {'object_name': 'FaultSourceTrace'},
            'geom': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'observations.faultsummary': {
            'Meta': {'object_name': 'FaultSummary'},
            'fid': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.IntegerField', [], {'default': "'-1'", 'max_length': '100', 'blank': 'True'})
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
            'slipType': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
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
            'geom': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {}),
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
        },
        'observations.foldsection': {
            'Meta': {'object_name': 'FoldSection'},
            'all_com': ('django.db.models.fields.IntegerField', [], {}),
            'compiler': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'contrib': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'created': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
            'dip_limbs': ('django.db.models.fields.IntegerField', [], {}),
            'dip_axial': ('django.db.models.fields.IntegerField', [], {}),
            'episodi_ac': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'episodi_is': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sec_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_max': ('django.db.models.fields.FloatField', [], {}),
            'length_min': ('django.db.models.fields.FloatField', [], {}),
            'length_pre': ('django.db.models.fields.FloatField', [], {}),
            'fold_type': ('django.db.models.fields.CharField', [], {}),
            'symmetry' : ('django.db.models.fields.CharField', [], {}),
            'dip_axial': ('django.db.models.fields.IntegerField', [], {}),
            'dip_limbs': ('django.db.models.fields.IntegerField', [], {}),
            'plunge': ('django.db.models.fields.IntegerField', [], {}),
            'tilt_rate': ('django.db.models.fields.IntegerField', [], {}),
            'growth_vert': ('django.db.models.fields.IntegerField', [], {}),
            'growth_hori': ('django.db.models.fields.IntegerField', [], {}),
            'surf_age': ('django.db.models.fields.IntegerField', [], {}),
            'mov_min': ('django.db.models.fields.IntegerField', [], {}),
            'mov_max': ('django.db.models.fields.IntegerField', [], {}),
            'mov_pref': ('django.db.models.fields.IntegerField', [], {}),
        },
        'observations.fold': {
            'Meta': {'object_name': 'Fold'},
            'all_com': ('django.db.models.fields.IntegerField', [], {}),
            'aseis_com': ('django.db.models.fields.IntegerField', [], {}),
            'aseis_slip': ('django.db.models.fields.FloatField', [], {}),
            'compiler': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'contrib': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'created': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3'}),
            'dip_com': ('django.db.models.fields.IntegerField', [], {}),
            'dip_dir': ('django.db.models.fields.IntegerField', [], {}),
            'dip_max': ('django.db.models.fields.IntegerField', [], {}),
            'dip_min': ('django.db.models.fields.IntegerField', [], {}),
            'dip_pref': ('django.db.models.fields.IntegerField', [], {}),
            'dis_max': ('django.db.models.fields.FloatField', [], {}),
            'dis_min': ('django.db.models.fields.FloatField', [], {}),
            'episodi_ac': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'episodi_is': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'fold_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_max': ('django.db.models.fields.FloatField', [], {}),
            'length_min': ('django.db.models.fields.FloatField', [], {}),
            'length_pre': ('django.db.models.fields.FloatField', [], {}),
            'low_d_com': ('django.db.models.fields.FloatField', [], {}),
            'low_d_max': ('django.db.models.fields.FloatField', [], {}),
            'low_d_min': ('django.db.models.fields.FloatField', [], {}),
            'low_d_pref': ('django.db.models.fields.FloatField', [], {}),
            're_int_max': ('django.db.models.fields.IntegerField', [], {}),
            're_int_min': ('django.db.models.fields.IntegerField', [], {}),
            're_int_pre': ('django.db.models.fields.IntegerField', [], {}),
            'slip_com': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_com': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_max': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_min': ('django.db.models.fields.IntegerField', [], {}),
            'slip_r_pre': ('django.db.models.fields.IntegerField', [], {}),
            'slip_typ': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'strike': ('django.db.models.fields.IntegerField', [], {}),
            'u_sm_d_com': ('django.db.models.fields.FloatField', [], {}),
            'u_sm_d_max': ('django.db.models.fields.FloatField', [], {}),
            'u_sm_d_min': ('django.db.models.fields.FloatField', [], {}),
            'u_sm_d_pre': ('django.db.models.fields.FloatField', [], {}),
            'fold_type': ('django.db.models.fields.CharField', [], {}),
            'symmetry' : ('django.db.models.fields.CharField', [], {}),
            'asymm_dir': ('django.db.models.fields.CharField', [], {}),
        },
    }

    complete_apps = ['observations']
