from odoo import models,fields


class HmsDoctors(models.Model):
    _name = "hms.doctors"
    _rec_name="first_name"

    first_name=fields.Char(string="first name")
    last_name=fields.Char(string="last name")
    image = fields.Image(max_height=400, max_width=400, verify_resolution=True)

    #log_ids = fields.One2many("hms.log.history" ,"doctor_id")



"""
class HmsLogHistory(models.Model):
    _name="hms.log.history"

    _rec_name="date"

    createdby=fields.Char(related="doctor_id.first_name" ,string="Created By")

    date=fields.Date()

    description=fields.Text()
    patient_id = fields.Many2one("hms.patient")
    doctor_id=fields.Many2one("hms.doctors")

"""