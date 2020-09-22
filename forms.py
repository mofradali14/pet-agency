from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class AddPetForm(FlaskForm):
    name = StringField('Name')
    species = SelectField('Species', choices=[
                          ('cat', 'Cat'), ('dog', 'Dog'), ('porc', 'Porcupine')])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[NumberRange(
        min=0, max=30, message='Age has to be between 0 and 30 years'), Optional()])
    notes = StringField('Notes')
    available = BooleanField('Available')


class EditPetForm(FlaskForm):
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    notes = StringField('Notes')
    available = BooleanField('Available')
