from openerp import models, fields, api

class next_of_kin(models.Model):
    _name = 'next.of.kin'

    name = fields.Char()
    relationship = fields.Many2one('next.of.kin.relationship')#Selection([('kin',"Kin"),('relative',"Relative"),('friend',"Friend")])
    beneficiary = fields.Boolean()
    date_of_birth = fields.Date()
    address = fields.Char()
    telephone = fields.Char()
    fax = fields.Char()
    email = fields.Char()

    idno = fields.Char()
    percentage_allocation = fields.Float()
    creation_date = fields.Date()
    member_no = fields.Char(string = 'Member ID')
    member_application_id = fields.Char(string = 'Member ID')

class next_of_kin_relationship(models.Model):
    _name = 'next.of.kin.relationship'

    name = fields.Char()
    description = fields.Char()

