from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired


class AddDepForm(FlaskForm):
    title = StringField('Название департамента', validators=[DataRequired()])
    email = EmailField("Почта департамента")
    members = StringField("Список id участников")
    chief = IntegerField("Id руководителя")
    submit = SubmitField('Применить')