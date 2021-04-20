from odoo import api, fields, models
from odoo.exceptions import ValidationError


class HmsCustomer(models.Model):
    _inherit = "res.partner"

    email=fields.Char()
    patient_id = fields.Many2one("hms.patient")
    related_patient_id = fields.Integer(related ="patient_id.id")
    website=fields.Char()

    # @api.model
    # def unlink(self):
    #     for rec in self:
    #        chk=rec.env["hms.patient"].search([("id","=",rec.patient_id.id)])
    #
    #     if chk:
    #         raise ValidationError('Not a valid E-mail')
    #
    #     else:
    #         return super().unlink()

    def unlink(self):
        chk = self.env['hms.patient'].search([("id", "=", self.related_patient_id)])
        if chk:
            raise ValidationError('Cant delete this customer')
        else:
            return super().unlink()

    @api.onchange('email')
    def check_email(self):
        chk = self.env['hms.patient'].search([("email", "=", self.email)])
        if chk:
            raise ValidationError("this mail is exist")
