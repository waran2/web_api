#from flask_wtf import Form
#from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, SelectField
#from wtforms import validators, ValidationError
from wtforms.fields.html5 import DateField
from FlaskWebProject import data

shops = [(30, 'Marble ArchMMM'), (10472, '1Stansted Airportyyyyyy')]
#shops = data.get_shops(1)

class BenchForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    name2 = TextField('Name:', validators=[validators.required()])
    shop_name = SelectField('Shop name:', choices = shops)
    production_no = SelectField('Production no:', choices = [(1,1),(2,2),(3,3),(4,4)])
    dt = DateField('DatePicker', format='%Y-%m-%d')
    submit = SubmitField("Send")

# form class with static fields
#class MyForm(FlaskForm):
#    name = StringField('static field')

#    record = {'field1': 'label1', 'field2': 'label2'}

# add dynamic fields
#    for key, value in record.items():
#        setattr(MyForm, key, StringField(value))
