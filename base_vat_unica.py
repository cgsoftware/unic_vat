# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    Copyright (C) 2008-2009 B2CK, Cedric Krier, Bertrand Chenal (the methods "check_vat_[a-z]{2}"
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
import string

from osv import osv, fields
from tools.translate import _



class res_partner(osv.osv):
    _inherit = 'res.partner'


    
    def _check_unic_vat(self, cr, uid, ids):
        #import pdb;pdb.set_trace()
        for session in self.browse(cr, uid, ids):
          if session.vat:
            res = self.search(cr, uid, [ ('vat','=',session.vat)
                                       ])
            # Result will contain the current session, we remove it here.
            res.remove( session.id )
            if len(res):
                # If we have any results left
                # we have duplicate entries
                return False
        return True
    
    def _check_unic_fiscalcode(self, cr, uid, ids):
        # import pdb;pdb.set_trace()
        for session in self.browse(cr, uid, ids):
          if session.fiscalcode:
            res = self.search(cr, uid, [ ('fiscalcode','=',session.fiscalcode)
                                       ])
            # Result will contain the current session, we remove it here.
            res.remove( session.id )
            if len(res):
                # If we have any results left
                # we have duplicate entries
                return False
        return True    

    _constraints = [(_check_unic_vat,
                    _('Questa Partita Iva Esiste Già'),
                    ['vat']),
                    (_check_unic_fiscalcode,
                    _('Questo Codice Fiscale Esiste Già'),
                    ['fiscalcode'])
                    
                   ]
  
res_partner()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
