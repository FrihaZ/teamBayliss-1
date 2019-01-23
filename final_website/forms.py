from wtforms import Form, StringField, SelectField

class KinaseSearchForm(Form):
    choices = [('Kinase', 'Kinase'), ('Family', 'Family'), ('Alias Name', 'Alias Name')]
    select = SelectField('Search for Kinase:', choices=choices)
    search = StringField('')

class InhibitorSearchForm(Form):
    choices = [('CHEMBL ID', 'CHEMBL ID')]
    select = SelectField('Search for Inhibitor:', choices=choices)
    search = StringField('')

class PhosphositeSearchForm(Form):
    choices = [('Kinase', 'Kinase'), ('Substrate', 'Substrate')]
    select = SelectField('Search for Inhibitor:', choices=choices)
    search = StringField('')
