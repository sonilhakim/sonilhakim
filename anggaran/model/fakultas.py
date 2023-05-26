from odoo import tools
from odoo import fields, models, api
import odoo.addons.decimal_precision as dp
import time
import logging
from odoo.tools.translate import _
from odoo.osv import expression

_logger = logging.getLogger(__name__)

class fakultas(models.Model):
    _name 		= "anggaran.fakultas"

    code		= fields.Char(string='Kode', required=True)
    name		= fields.Char(string='Nama', required=True)
    alamat		= fields.Char(string='Alamat')
    nama_bank	= fields.Char(string='Nama Bank')
    nomor_rek	= fields.Char(string='No Rekening')



    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):

        args = args or []
        domain = []
        if name:
            domain = ['|', ('code', operator, name), ('name', operator, name)]
            if operator in expression.NEGATIVE_TERM_OPERATORS:
                domain = ['&', '!'] + domain[1:]
        rec_ids = self._search(expression.AND([domain, args]), limit=limit, access_rights_uid=name_get_uid)
        return self.browse(rec_ids).name_get()


    @api.multi
    def name_get(self):
        result = []
        for rec in self:
            name = rec.code + ' ' + rec.name
            result.append((rec.id, name))
        return result


