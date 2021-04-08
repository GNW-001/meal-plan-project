from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import TextField, TextAreaField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, InputRequired

class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[Length(min=6, max=35)])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password')
    weight = StringField('Weight (lbs)', validators=[DataRequired()])
    height = StringField('Height (cm)', validators=[DataRequired()])
    profPic = FileField('Profile Picture', validators=[FileAllowed(['png', 'jpg','Images only!'])])

class LoginForm(FlaskForm):
    email = StringField('email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class RecipeForm(FlaskForm):
    name = StringField('Recipe Name', validators=[DataRequired()])
    instruction = TextAreaField('Instructions',validators=[DataRequired()])
    numInstruction = StringField('No. of Instructions', validators=[DataRequired()])
    ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
    measurement = StringField('Unit of Measurement', validators=[DataRequired()])
    numMeasurement = StringField('Amount Being Used', validators=[DataRequired()])