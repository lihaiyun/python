# Note: Use wtforms v3.0.0
from wtforms import Form, StringField, PasswordField, RadioField, SelectField, TextAreaField, validators, EmailField, DateField


class CreateUserForm(Form):
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.Length(min=6, max=15), validators.DataRequired()])
    confirm_password = PasswordField('Confirm Password', [validators.Length(min=6, max=15), validators.DataRequired(),
                                                          validators.EqualTo('password',
                                                                             message='Passwords must match.')])
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()],
                         choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    birthday = DateField('Birthday', [validators.Optional()])
    membership = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')],
                            default='F')
    remarks = TextAreaField('Remarks', [validators.Optional()])
