#!/usr/bin/python
# -*- encoding: utf-8 -*-
###############################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#    Copyright (C) OpenERP Venezuela (<http://www.vauxoo.com>).
#    All Rights Reserved
############# Credits #########################################################
#    Coded by: Katherine Zaoral <kathy@vauxoo.com>
#    Planified by: Humberto Arocha <hbto@vauxoo.com>
#    Audited by: Humberto Arocha <hbto@vauxoo.com>
###############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################

{
    'name': 'Purchase Requisition Currency',
    'version': '1.0',
    'author': 'Vauxoo',
    'website': 'http://www.vauxoo.com/',
    'category': '',
    'description': '''
Purchase Requisition Currency
=============================

This module add the currency field in the purchase requisition model.
You need to active some user technical settings to take advantage of this
functionality:
  - Multi Currencies.
  - Purchase Pricelist.
''',
    'depends': [
        'purchase_requisition',
        ],
    'data': [
        'view/purchase_requisition_view.xml',
        ],
    'demo': [],
    'test': [],
    'qweb': [],
    'js': [],
    'css': [],
    'active': False,
    'installable': True,
}
