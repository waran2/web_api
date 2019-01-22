from flask import Flask, render_template, request, flash
from FlaskWebProject import app, forms
from datetime import datetime



@app.route("/", methods=['GET', 'POST'])



def hello():

    f= open("log_file.txt","w+")

    for i in range(10):
        now = datetime.now().strftime('%d-%m-%y %H:%M:%S')
        f.write("This is line %d\r\n" % (i+1))
        f.write("The date and time is %s\r\n" % (now))

    f.close()

    form = forms.BenchForm(request.form)

    print (form.errors)
    if request.method == 'POST':
        name=request.form['shop_name']
        print (name)

    #if form.validate():
        # Save the comment here.
        flash('Hello ' + name)
    #    else:
    #    flash('All the form fields are required. ')



    return render_template('hello.html', form=form)
