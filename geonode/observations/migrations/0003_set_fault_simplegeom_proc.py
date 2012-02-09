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
       db.execute("""
CREATE FUNCTION set_fault_simplegeom(target_fault_id integer) RETURNS VOID AS $$
DECLARE
    sections_united geometry;
BEGIN
    SELECT
        ST_Union(fault_section_view.geom)
    FROM
        gem.fault_section_view
        JOIN
        gem.observations_faultsection_fault
        ON (fault_section_view.id = observations_faultsection_fault.faultsection_id)
    WHERE
        observations_faultsection_fault.fault_id = target_fault_id
    INTO
        sections_united;

    UPDATE
        gem.observations_fault
    SET
        simple_geom = ST_Multi(ST_LongestLine(sections_united, sections_united))
    WHERE
        id = target_fault_id;
END;
$$ LANGUAGE plpgsql VOLATILE STRICT;
        """)

    def backwards(self, orm):
        db.execute("DROP FUNCTION set_fault_simplegeom")

    models = {}

    complete_apps = ['observations']
