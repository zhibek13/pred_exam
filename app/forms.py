from flask_wtf import FlaskForm
import wtforms as wf


class UserForm(FlaskForm):
    username = wf.StringField('Пользователь', validators=[wf.validators.DataRequired()])
    password = wf.PasswordField('Пароль', validators=[
        wf.validators.DataRequired(),
        wf.validators.Length(min=3, max=64)
    ])
    submit = wf.SubmitField('OK')


class CustomerForm(FlaskForm):
    name = wf.StringField('Имя', validators=[wf.validators.DataRequired()])
    phone_number = wf.IntegerField('Номер телефона', validators=[wf.validators.DataRequired()])
    item = wf.StringField('Наименование товара', validators=[wf.validators.DataRequired()])
    quantity = wf.IntegerField('Количество товара', validators=[wf.validators.DataRequired()])
    price = wf.IntegerField('Цена товара', validators=[wf.validators.DataRequired()])
    submit = wf.SubmitField('OK')
