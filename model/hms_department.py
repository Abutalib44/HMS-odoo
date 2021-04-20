from odoo import models,fields


class HmsDepartment(models.Model):
    _name="hms.deprtment"
    _description="Deprtment"

    name = fields.Char(string="Name" )
    capacity=fields.Integer()
    is_opend=fields.Boolean()

    patient_ids = fields.One2many("hms.patient","department_id")
