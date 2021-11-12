import os
from forms import  AddForm , DelForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

########### MODELS

class Puppy(db.Model):

    __tablename__ = "puppies"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner',backref='puppy',uselist=False)
    
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"Puppy name is {self.name}"

class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,name,puppy_id):
        self.name=name
        self.puppy_id=puppy_id

    def __repr__(self):
        return f"Owner name is {self.name}"

#################################
#### VIEW FUNCTIONS WITH FORMS ####

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add',methods=['GET','POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()
        
        return redirect(url_for('list_puppies'))

    return render_template('addpuppies.html', form=form)

@app.route('/del',methods=['GET','POST'])
def deletepup():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()
        
        return redirect(url_for('list_puppies'))

    return render_template('deletepuppies.html', form=form)

@app.route('/list')
def list_puppies():
    
    puppies = Puppy.query.all()

    return render_template('listpuppies.html',puppies=puppies)






if __name__ == '__main__':
    app.run(debug=True)
