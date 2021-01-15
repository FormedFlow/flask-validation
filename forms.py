from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length

class registerForm(FlaskForm):
    username = StringField('Никнейм: ', validators=[DataRequired(), Length(min=4, max=120)])
    msg = PasswordField('Пароль: ', validators=[DataRequired(), Length(min=6, max=15)])
    submit = SubmitField('Отправить')


