from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import TextField, TextAreaField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length

class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[Length(min=6, max=35)])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password')
    weight = StringField('Weight (lbs)', validators=[DataRequired()])
    height = StringField('Height (cm)', validators=[DataRequired()])
    profPic = FileField('Profile Picture',validators=[FileRequired(), FileAllowed(['png', 'jpg','Images only!'])])