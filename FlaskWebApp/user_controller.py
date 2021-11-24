from flask import Blueprint, render_template, request, redirect, url_for
from user_forms import CreateUserForm
from user import User
import shelve

user_controller = Blueprint('user', __name__)


def read_users():
    user_dict = {}
    db = shelve.open('library')
    if 'users' in db:
        user_dict = db['users']
    db.close()
    return user_dict


def save_users(user_dict):
    db = shelve.open('library')
    db['users'] = user_dict
    db.close()


@user_controller.route('/retrieveUsers')
def retrieve_users():
    user_dict = read_users()
    user_list = user_dict.values()
    return render_template('retrieveUsers.html', count=len(user_list), user_list=user_list)


@user_controller.route('/createUser', methods=['GET', 'POST'])
def create_user():
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        user_dict = read_users()

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

        save_users(user_dict)
        return redirect(url_for('home'))
    return render_template('createUser.html', form=create_user_form)
