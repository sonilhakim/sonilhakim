#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class aset(models.Model):

    _name = "account.asset.asset"
    _description = "account.asset.asset"

    _inherit = "account.asset.asset"

