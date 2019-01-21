from flask import Flask, render_template, request
#from forms import  BenchForm
from FlaskWebProject import app

from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, SelectField
#from wtforms import validators, ValidationError
from wtforms.fields.html5 import DateField

class BenchForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    name2 = TextField('Name:', validators=[validators.required()])


@app.route("/", methods=['GET', 'POST'])



def hello():
    form = BenchForm(request.form)

    print (form.errors)
    if request.method == 'POST':
        name=request.form['name']
        print (name)

    #if form.validate():
        # Save the comment here.
        flash('Hello ' + name)
    #    else:
    #    flash('All the form fields are required. ')

    return render_template('hello.html', form=form)
