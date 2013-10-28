#!/usr/bin/python
# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#    Copyright (C) Vauxoo (<http://vauxoo.com>).
#    All Rights Reserved
###############Credits######################################################
#    Coded by: Luis Ernesto García Medina(ernesto_gm@vauxoo.com)
#############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
################################################################################

{
    "name" : "supplier_invoice_number_unique",
    "version" : "1.0",
    "author" : "Vauxoo",
    "category" : "Accouting",
    "description" : """
This module validates that the supplier_invoice_number field is not repeated 
============================================================================
The validation doesn't consider uppercase and lowercase, if you have one invoice with supplier 
invoice number:  "A123" and you try validate another invoice with the supplier 
invoice number: "a123", the validation is going to show the message: "Error you can not validate 
the invoice with supplier invoice number duplicated"
    """,
    "website" : "http://www.vauxoo.com/",
    "license" : "AGPL-3",
    "depends" : [
        "account",
    ],
    "demo" : [],
    "data" : [
    'view/account_invoice_view.xml',
    ],
    "installable" : True,
    "active" : False,
}
