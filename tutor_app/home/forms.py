from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField("email", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    submit = SubmitField("submit")

class RegisterForm(FlaskForm):
    email = StringField("email", validators=[DataRequired()])
    first_name = StringField("first name", validators=[DataRequired()])
    last_name = StringField("last name", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    confirm_password = PasswordField("confirm password", validators=[DataRequired()])
    submit = SubmitField("submit")