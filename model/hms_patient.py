from odoo import models,fields,api
import re
from odoo.exceptions import ValidationError
from datetime import date, timedelta,datetime
# from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

class HmsPatient(models.Model):
    _name="hms.patient"
    _sql_constraints = [('email_unique', 'UNIQUE(email)', "The Email must be unique"), ]

    _rec_name="first_name"
    first_name=fields.Char(string="First Name" ,required=True)
    last_name=fields.Char(string="Last Name" ,required=True)
    birth_date=fields.Date()
    history=fields.Html(string="History")
    cr_ratio=fields.Float()
    blod_type=fields.Selection([
        ('typeA','A'),
        ('typeB','B'),
        ('typeAB','AB'),
        ('typeO','O')
    ]
    ,string="Blod Type")
    pcr=fields.Boolean()
    image=fields.Image(max_height=400,max_width=400,verify_resolution=True)
    address=fields.Text(string="Address")
    age=fields.Integer(string="Age")
    state = fields.Selection(string="State", selection=[('undetrmined', 'undetrmined'), ('Good', 'Good'),('Fair', 'Fair'),('Serious', 'Serious') ])
    capacity_dept =fields.Integer(related="department_id.capacity")
    department_id = fields.Many2one("hms.deprtment")
    #log_ids = fields.One2many("hms.log.history","patient_id")
    doctors_ids = fields.Many2many("hms.doctors")
    email=fields.Char(required=True)

    @api.onchange('age')
    def onchange_age(self):
        if self.age > 0 and self.age < 30:
            self.pcr = True
            return {
                "warning": {
                    "title": "Take Care",
                    "message": "your pcr is checked"
                }
            }
        else:
            self.pcr = False

#this make a record in log when change in state
    @api.onchange('state')
    def onchange_state(self):
        if self.state:
            description="The Patient {} update state to {}".format(self.first_name,self.state)
            val={
                "description":description
            }
            self.env["hms.log"].create(val)

                    # result=fields.Text()



    @api.onchange('email')
    def validate_mail(self):
        if self.email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
            if match == None:
                raise ValidationError('Not a valid E-mail')


    # @api.onchange('birth_date')
    # def calculate_age(self):
    #     age = (date.today() - self.birth_date) // timedelta(days=365.2425)
    #     self.age = age

    @api.onchange('birth_date')
    def set_age(self):
        for rec in self:
            if rec.birth_date:
                dt = str(rec.birth_date)
                d1 = datetime.strptime(dt, "%Y-%m-%d").date()
                d2 = date.today()
                rd = relativedelta(d2, d1)
                rec.age = rd.years





