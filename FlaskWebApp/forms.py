from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators


class CreateUserForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()],
                         choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    membership = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')],
                            default='F')
    remarks = TextAreaField('Remarks', [validators.Optional()])
