from flask import Flask, render_template, request, flash
from FlaskWebProject import app, forms



@app.route("/", methods=['GET', 'POST'])



def hello():
    form = forms.BenchForm(request.form)

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
