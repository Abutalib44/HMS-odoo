from odoo import models,fields


class HmsLogHistory(models.Model):
    _name="hms.log"

    create_uid = fields.Integer(string="Created By")
    create_date = fields.Date(string="Date")
    description = fields.Text(string="Description")
