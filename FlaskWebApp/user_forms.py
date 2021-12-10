# Note: Use wtforms v3.0.0
from wtforms import Form, StringField, PasswordField, RadioField, SelectField, TextAreaField, EmailField, DateField, \
    validators
from user import User


class CreateUserForm(Form):
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.Length(min=6, max=15), validators.DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', [validators.Length(min=6, max=15), validators.DataRequired(),
                             validators.EqualTo('password', message='Passwords must match.')])
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=User.gender_dict.items(), default='')
    birthday = DateField('Birthday', [validators.Optional()])
    membership = RadioField('Membership', choices=User.membership_dict.items(), default='F')
    user_type = RadioField('User Type', choices=User.user_type_dict.items(), default='C')
    remarks = TextAreaField('Remarks', [validators.Optional()])


class UpdateUserForm(Form):
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=User.gender_dict.items(), default='')
    birthday = DateField('Birthday', [validators.Optional()])
    membership = RadioField('Membership', choices=User.membership_dict.items(), default='F')
    user_type = RadioField('User Type', choices=User.user_type_dict.items(), default='C')
    remarks = TextAreaField('Remarks', [validators.Optional()])


class LoginForm(Form):
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.Length(min=6, max=15), validators.DataRequired()])
