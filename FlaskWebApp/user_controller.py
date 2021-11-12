from flask import Blueprint, render_template, request, redirect, url_for
from user_forms import CreateUserForm
from user import User
import shelve

user_controller = Blueprint('user', __name__)


@user_controller.route('/createUser', methods=['GET', 'POST'])
def create_user():
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        user_dict = {}
        db = shelve.open('library')
        if 'users' in db:
            user_dict = db['users']

        email = create_user_form.email.data
        password = create_user_form.password.data
        name = create_user_form.name.data
        gender = create_user_form.gender.data
        birthday = create_user_form.birthday.data
        membership = create_user_form.membership.data
        remarks = create_user_form.remarks.data
        user = User(email, password, name, gender, membership, remarks, birthday)
        print(user)

        user_dict[user.id] = user
        db['users'] = user_dict
        db.close()

        return redirect(url_for('home'))
    return render_template('createUser.html', form=create_user_form)
