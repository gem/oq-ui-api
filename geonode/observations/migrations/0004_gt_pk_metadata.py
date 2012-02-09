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
        CREATE TABLE gem.gt_pk_metadata (
            table_schema VARCHAR(32) NOT NULL,
            table_name VARCHAR(32) NOT NULL,
            pk_column VARCHAR(32) NOT NULL,
            pk_column_idx INTEGER,
            pk_policy VARCHAR(32),
            pk_sequence VARCHAR(64),
            unique (table_schema, table_name, pk_column),
            check (pk_policy in ('sequence', 'assigned', 'autoincrement'))
        )
        """)
        db.execute("""
        INSERT INTO
            gem.gt_pk_metadata (table_schema, table_name, pk_column)
        VALUES
            ('gem', 'fault_section_view', 'id')
        """)
        db.execute("""
        INSERT INTO
            gem.gt_pk_metadata (table_schema, table_name, pk_column)
        VALUES
            ('gem', 'fault_view', 'id')
        """)


    def backwards(self, orm):
        db.execute("DROP TABLE gem.gt_pk_metadata")


    models = {}

    complete_apps = ['observations']
