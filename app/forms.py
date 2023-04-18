from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class signupForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired()])
    password = StringField('Password', validators = [DataRequired()])
    confirm_password = StringField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = StringField()