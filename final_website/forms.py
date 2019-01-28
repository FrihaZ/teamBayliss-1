from wtforms import Form, StringField, SelectField
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from wtforms import validators

class KinaseSearchForm(Form):
    choices = [('Kinase', 'Kinase'), ('Family', 'Family'), ('Alias Name', 'Alias Name'),
                ('Uniprot ID', 'Uniprot ID')]
    select = SelectField('Search for Kinase:', choices=choices)
    search = StringField('',[validators.DataRequired()])

class InhibitorSearchForm(Form):
    choices = [(' ChEMBL ID ', ' ChEMBL ID ')]
    select = SelectField('Search for Inhibitor:', choices=choices)
    search = StringField('')

class PhosphositeSearchForm(Form):
    choices = [('Substrate', 'Substrate')]
    select = SelectField('Search for Phosphosite:', choices=choices)
    search = StringField('')
