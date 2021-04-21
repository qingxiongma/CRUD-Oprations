from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.fields.html5 import EmailField 
from wtforms.validators import DataRequired, Length, Email
from email_validator import validate_email, EmailNotValidError


class ContactForm(FlaskForm):
    """Contact form."""
    name = StringField('Name', [
        DataRequired()])
    email = EmailField('Email', [
        DataRequired(),
        Email()])
    body = TextField('Message', [
        DataRequired(),
        Length(min=4, message=('Your message is too short.'))])
    submit = SubmitField('Submit')

class StudentForm(FlaskForm):
    name = StringField('Name', [
        DataRequired()])
    phone = StringField('Phone', [
        DataRequired()])
    email = EmailField('Email', [
        DataRequired(),
        Email()])
    address = StringField('Address', [
        DataRequired()])
    submit = SubmitField('Submit')
    