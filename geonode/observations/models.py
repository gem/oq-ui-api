# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

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

from django.contrib.gis.db import models

#observation db
#fault tables


class FaultSource(models.Model):
    fault = models.ForeignKey('Fault')
    source_nm  = models.CharField(max_length=30)
    fault_name = models.CharField(max_length=30)

    length_min = models.FloatField(null=True, blank=True)
    length_max = models.FloatField(null=True, blank=True)
    length_pre = models.FloatField(null=True, blank=True)

    # Upper seismogenic depth
    u_sm_d_min = models.FloatField(null=True, blank=True)
    u_sm_d_max = models.FloatField(null=True, blank=True)
    u_sm_d_pre = models.FloatField(null=True, blank=True)
    u_sm_d_com = models.FloatField(null=True, blank=True)

    # Lower seismogenic depth
    low_d_min = models.FloatField(null=True, blank=True)
    low_d_max = models.FloatField(null=True, blank=True)
    low_d_pref = models.FloatField(null=True, blank=True)
    low_d_com = models.FloatField(null=True, blank=True)

    width_min = models.FloatField(null=True, blank=True)
    width_max = models.FloatField(null=True, blank=True)
    width_pref = models.FloatField(null=True, blank=True)

    area_min = models.FloatField(null=True, blank=True)
    area_max = models.FloatField(null=True, blank=True)
    area_pref = models.FloatField(null=True, blank=True)

    dip_min = models.IntegerField(null=True, blank=True)
    dip_max = models.IntegerField(null=True, blank=True)
    dip_pref = models.IntegerField(null=True, blank=True)
    dip_com = models.IntegerField(null=True, blank=True)
    dip_dir = models.IntegerField(null=True, blank=True)

    slip_typ = models.CharField(max_length=30, default='')
    slip_com = models.IntegerField(null=True, blank=True)
    slip_r_min = models.FloatField(null=True, blank=True)
    slip_r_max = models.FloatField(null=True, blank=True)
    slip_r_pre = models.FloatField(null=True, blank=True)
    slip_r_com = models.FloatField(null=True, blank=True)

    # Magnitude
    mag_min = models.FloatField(null=True, blank=True)
    mag_max = models.FloatField(null=True, blank=True)
    mag_pref = models.FloatField(null=True, blank=True)

    # Seismic moment
    mom_min = models.FloatField(null=True, blank=True)
    mom_max = models.FloatField(null=True, blank=True)
    mom_pref = models.FloatField(null=True, blank=True)

    aseis_slip = models.FloatField(null=True, blank=True)
    aseis_com = models.IntegerField(null=True, blank=True)

    # Displacement
    dis_min = models.FloatField(null=True, blank=True)
    dis_max = models.FloatField(null=True, blank=True)
    dis_pref = models.FloatField(null=True, blank=True)

    # Recurrence Interval
    re_int_min = models.IntegerField(null=True, blank=True)
    re_int_max = models.IntegerField(null=True, blank=True)
    re_int_pre = models.IntegerField(null=True, blank=True)

    # Age of last movement
    mov_min = models.IntegerField(null=True, blank=True)
    mov_max = models.IntegerField(null=True, blank=True)
    mov_pref = models.IntegerField(null=True, blank=True)

    all_com = models.IntegerField(null=True, blank=True)

    compiler = models.CharField(max_length=30, default='')
    contrib = models.CharField(max_length=30, default='')

    geom = models.PolygonField(srid=4326)
    created = models.DateField(null=True, blank=True)


class Fault(models.Model):
    fault_name = models.CharField(max_length=30, null=True, blank=True)
    length_min = models.FloatField(null=True, blank=True)
    length_max = models.FloatField(null=True, blank=True)
    length_pre = models.FloatField(null=True, blank=True)
    strike = models.IntegerField(null=True, blank=True)
    episodi_is = models.CharField(max_length=30, null=True, blank=True)
    episodi_ac = models.CharField(max_length=30, null=True, blank=True)
    u_sm_d_min = models.FloatField(null=True, blank=True)
    u_sm_d_max = models.FloatField(null=True, blank=True)
    u_sm_d_pre = models.FloatField(null=True, blank=True)
    u_sm_d_com = models.FloatField(null=True, blank=True)
    low_d_min = models.FloatField(null=True, blank=True)
    low_d_max = models.FloatField(null=True, blank=True)
    low_d_pref = models.FloatField(null=True, blank=True)
    low_d_com = models.FloatField(null=True, blank=True)
    dip_min = models.IntegerField(null=True, blank=True)
    dip_max = models.IntegerField(null=True, blank=True)
    dip_pref = models.IntegerField(null=True, blank=True)
    dip_com = models.IntegerField(null=True, blank=True)
    dip_dir = models.IntegerField(null=True, blank=True)
    down_thro = models.IntegerField(null=True, blank=True)
    slip_typ = models.CharField(max_length=30)
    slip_com = models.IntegerField(null=True, blank=True)
    slip_r_min = models.FloatField(null=True, blank=True)
    slip_r_max = models.FloatField(null=True, blank=True)
    slip_r_pre = models.FloatField(null=True, blank=True)
    slip_r_com = models.FloatField(null=True, blank=True)
    aseis_slip = models.FloatField(null=True, blank=True)
    aseis_com = models.IntegerField(null=True, blank=True)
    dis_min = models.FloatField(null=True, blank=True)
    dis_max = models.FloatField(null=True, blank=True)
    dis_pref = models.FloatField(null=True, blank=True)
    re_int_min = models.IntegerField(null=True, blank=True)
    re_int_max = models.IntegerField(null=True, blank=True)
    re_int_pre = models.IntegerField(null=True, blank=True)
    mov_min = models.IntegerField(null=True, blank=True)
    mov_max = models.IntegerField(null=True, blank=True)
    mov_pref = models.IntegerField(null=True, blank=True)
    all_com = models.IntegerField(null=True, blank=True)
    compiler = models.CharField(max_length=30, null=True, blank=True)
    contrib = models.CharField(max_length=30, null=True, blank=True)
    created = models.DateField(null=True, blank=True)
    simple_geom = models.MultiLineStringField(srid=4326, null=True, blank=True)

    def __unicode__(self):
        return "Fault %s %s" % (self.pk, self.fault_name)

class FaultSection(models.Model):
    fault = models.ManyToManyField('Fault')
    sec_name = models.CharField(max_length=255, null=True, blank=True)
    length_min = models.FloatField(null=True, blank=True)
    length_max = models.FloatField(null=True, blank=True)
    length_pre = models.FloatField(null=True, blank=True)
    strike = models.IntegerField(null=True, blank=True)
    episodi_is = models.CharField(max_length=30, null=True, blank=True)
    episodi_ac = models.CharField(max_length=30, null=True, blank=True)
    u_sm_d_min = models.FloatField(null=True, blank=True)
    u_sm_d_max = models.FloatField(null=True, blank=True)
    u_sm_d_pre = models.FloatField(null=True, blank=True)
    u_sm_d_com = models.FloatField(null=True, blank=True)
    low_d_min = models.FloatField(null=True, blank=True)
    low_d_max = models.FloatField(null=True, blank=True)
    low_d_pref = models.FloatField(null=True, blank=True)
    low_d_com = models.FloatField(null=True, blank=True)
    dip_min = models.IntegerField(null=True, blank=True)
    dip_max = models.IntegerField(null=True, blank=True)
    dip_pref = models.IntegerField(null=True, blank=True)
    dip_com = models.IntegerField(null=True, blank=True)
    dip_dir = models.IntegerField(null=True, blank=True)
    down_thro = models.IntegerField(null=True, blank=True)
    slip_typ = models.CharField(max_length=30)
    slip_com = models.IntegerField(null=True, blank=True)
    slip_r_min = models.FloatField(null=True, blank=True)
    slip_r_max = models.FloatField(null=True, blank=True)
    slip_r_pre = models.FloatField(null=True, blank=True)
    slip_r_com = models.FloatField(null=True, blank=True)
    aseis_slip = models.FloatField(null=True, blank=True)
    aseis_com = models.IntegerField(null=True, blank=True)
    dis_min = models.FloatField(null=True, blank=True)
    dis_max = models.FloatField(null=True, blank=True)
    dis_pref = models.FloatField(null=True, blank=True)
    re_int_min = models.IntegerField(null=True, blank=True)
    re_int_max = models.IntegerField(null=True, blank=True)
    re_int_pre = models.IntegerField(null=True, blank=True)
    mov_min = models.IntegerField(null=True, blank=True)
    mov_max = models.IntegerField(null=True, blank=True)
    mov_pref = models.IntegerField(null=True, blank=True)
    all_com = models.IntegerField(null=True, blank=True)
    compiler = models.CharField(max_length=30, null=True, blank=True)
    contrib = models.CharField(max_length=30, null=True, blank=True)
    created = models.DateField(null=True, blank=True)


class Trace(models.Model):
    fault_section = models.ManyToManyField('FaultSection')
    loc_meth = models.CharField(max_length=30)
    scale = models.BigIntegerField()
    accuracy = models.BigIntegerField()
    notes = models.TextField()
    geom = models.MultiLineStringField(srid=4326)


class SiteObservation(models.Model):
    geom = models.PointField(srid=4326)
    fault_section = models.ForeignKey('FaultSection', blank=True, null=True)
    scale = models.BigIntegerField()
    accuracy = models.BigIntegerField()
    s_feature = models.CharField(max_length=30)
    notes = models.TextField()
