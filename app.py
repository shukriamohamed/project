from flask import Flask, render_template, url_for, flash, request, redirect # want to import flash messgae when form is submitted
'''
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField,PasswordField, BooleanField, ValidationError) #from wtforms import StringField, SubmitField  #stringfield textbox, submitfield is the submit button
from wtforms.validators import DataRequired, EqualTo,Length   #DataRequired is one type of validator to say something when someone doesn't fill out the box, Equalto is so the 2 passwords match and that there are certain length for the password
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime #to see the date time when things are imported into the DB
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash # want two things: we want to generate a hash which your password will turn into and we also want to check that hash to see if its the right one for your password 
from wtforms.widgets import TextArea
'''

app = Flask(__name__) 

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__': 
    app.run(debug=True) 