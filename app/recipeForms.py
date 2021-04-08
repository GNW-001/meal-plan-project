from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import TextField, TextAreaField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length

class RecipeForm(FlaskForm):
    name = StringField('Recipe Name', validators=[DataRequired()])
    instruction = TextAreaField('Instructions',validators=[DataRequired()])
    numInstruction = StringField('No. of Instructions', validators=[DataRequired()])
    ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
    measurement = StringField('Unit of Measurement', validators=[DataRequired()])
    numMeasurement = StringField('Amount Being Used', validators=[DataRequired()])