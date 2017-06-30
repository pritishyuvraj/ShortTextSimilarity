from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
 
# App config.
DEBUG = True
app = Flask(__name__, template_folder = './')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
 
'''
@app.route("/input", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
    print form.errors
    if request.method == 'POST':
        name=request.form['name']
        print name
 
        if form.validate():
            # Save the comment here.
            flash('Hello ' + name)
            test(name)
        else:
            flash('All the form fields are required. ')
 
    return render_template('input.php', form=form)
'''

@app.route("/try1", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
    if request.method == 'POST':
        S1 = request.form['sent1']
        S2 = request.form['sent2']
        if S1 and S2:
            write2file(S1, S2)
        print S1, S2 

    return render_template('input.php', form=form)

def write2file(S1, S2):
    text = "python sts1.py \"" + S1 + "\" \"" + S2 + " \""
    open('script.sh', 'w').close()
    f = open('script.sh', 'w')
    f.write(text)
    f.close()
    print "Done Writing"

    from subprocess import call
    call(['sh', 'script.sh'])

def test(name):
    flash( "Its working")

if __name__ == "__main__":
    app.run()