#!/usr/bin/python
# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#    Copyright (C) OpenERP Venezuela (<http://openerp.com.ve>).
#    All Rights Reserved
###############Credits######################################################
#    Coded by: Vauxoo C.A.           
#    Planified by: Nhomar Hernandez
#    Audited by: Vauxoo C.A.
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

import time
from osv import fields, osv
import decimal_precision as dp
from tools.translate import _
import netsvc

class account_invoice(osv.osv):
    _inherit = 'account.invoice'

    _columns = {
        'cancel_true':fields.boolean('Invoice Cancel',help="Field that indicates whether the invoice was canceled earlier, to generate actions automatically")
    
    }
    def action_number(self, cr, uid, ids, context=None):
        '''
        Modified to witholding vat validate 
        '''
        wf_service = netsvc.LocalService("workflow")
        res = super(account_invoice, self).action_number(cr, uid, ids, context=context)
        iva_line_obj = self.pool.get('account.wh.iva.line')
        iva_obj = self.pool.get('account.wh.iva')
        invo_brw = self.browse(cr,uid,ids,context=context)[0]
        if invo_brw.cancel_true:
            iva_line_obj.load_taxes(cr, uid, [i.id for i in invo_brw.wh_iva_id.wh_lines], context=context)
            wf_service.trg_validate(uid, 'account.wh.iva',invo_brw.wh_iva_id.id, 'wh_iva_confirmed', cr)
            wf_service.trg_validate(uid, 'account.wh.iva',invo_brw.wh_iva_id.id, 'wh_iva_done', cr)

        return res
    
    
    def check_iva_islr(self, cr, uid, ids, context=None):
        if context is None:
            context={}
        invo_brw = self.browse(cr,uid,ids[0],context=context)
        if invo_brw.islr_wh_doc_id and invo_brw.wh_iva_id:
            return False
        return True


account_invoice()

