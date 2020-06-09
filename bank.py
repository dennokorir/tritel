from openerp import models, fields, api
from openerp.exceptions import ValidationError
import base64
import io
import csv
#import openpyxl
import struct

class bank_statement(models.Model):
    _inherit = 'account.bank.statement'

    statement_file = fields.Binary('Bank Statement File')
    test = fields.Text()

    @api.one
    def process(self):
        if self.statement_file:
            f = open("spreadsheet.xls", "wb")
            f.write(self.statement_file.decode('base64'))
            f.close()
            e = open("spreadsheet.xls")
            next_line = e.readline()
            while next_line != "":
                line = next_line.split(",")
                #date,reference,name,amount,statement_id
                self.env['account.bank.statement.line'].create({'date':line[0],'ref':line[1],'name':line[2],'amount':line[3],'statement_id':self.id})
                next_line = e.readline()
        else:
            raise ValidationError('You must import .csv file before Processing Statement File')


