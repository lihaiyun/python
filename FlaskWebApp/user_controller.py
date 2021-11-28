from flask import Blueprint, render_template, request, redirect, url_for
from user_forms import CreateUserForm
from user import User
from user_service import get_user_list, save_user

user_controller = Blueprint('user', __name__)


@user_controller.route('/retrieveUsers')
def retrieve_users():
    user_list = get_user_list()
    return render_template('retrieveUsers.html', count=len(user_list), user_list=user_list)


@user_controller.route('/createUser', methods=['GET', 'POST'])
def create_user():
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        email = create_user_form.email.data
        password = create_user_form.password.data
        name = create_user_form.name.data
        gender = create_user_form.gender.data
        birthday = create_user_form.birthday.data
        membership = create_user_form.membership.data
        user_type = create_user_form.user_type.data
        remarks = create_user_form.remarks.data
        user = User(email, password, name, gender, membership, remarks, birthday, user_type)
        print(user)

        save_user(user)
        # return redirect('/retrieveUsers')
        return redirect(url_for('user.retrieve_users'))
    return render_template('createUser.html', form=create_user_form)
