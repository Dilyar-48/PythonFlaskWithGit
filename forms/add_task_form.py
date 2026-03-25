from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    title = StringField('Работа', validators=[DataRequired()])
    work_size = IntegerField("Размер работы")
    is_finished = BooleanField("Завершена")
    collaborators = StringField("Список id команды")
    team_leader = IntegerField("Id руководителя")
    category_id = IntegerField("Id категории")
    submit = SubmitField('Применить')