from flask import Flask, render_template, request
from forms import  ReusableForm


app = Flask(__name__)
app.secret_key = 'development key'

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

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



if __name__ == '__main__':
   app.run(debug = True)
