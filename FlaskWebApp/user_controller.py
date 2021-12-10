from flask import Blueprint, render_template, request, redirect, session
from user_forms import CreateUserForm, UpdateUserForm, LoginForm
from user import User
from user_service import get_user_list, get_user, save_user, get_user_for_login

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
        return redirect('/retrieveUsers')
    else:
        return render_template('createUser.html', form=create_user_form)


@user_controller.route('/updateUser/<id>', methods=['GET', 'POST'])
def update_user(id):
    user = get_user(id)
    update_user_form = UpdateUserForm(request.form)
    if request.method == 'POST' and update_user_form.validate():
        user.email = update_user_form.email.data
        user.name = update_user_form.name.data
        user.gender = update_user_form.gender.data
        user.birthday = update_user_form.birthday.data
        user.membership = update_user_form.membership.data
        user.user_type = update_user_form.user_type.data
        user.remarks = update_user_form.remarks.data
        print(user)
        save_user(user)
        return redirect('/retrieveUsers')
    else:
        update_user_form.email.data = user.email
        update_user_form.name.data = user.name
        update_user_form.gender.data = user.gender
        update_user_form.birthday.data = user.birthday
        update_user_form.membership.data = user.membership
        update_user_form.user_type.data = user.user_type
        update_user_form.remarks.data = user.remarks
        return render_template('updateUser.html', form=update_user_form)


@user_controller.route('/deleteUser/<id>', methods=['POST'])
def delete_user(id):
    user = get_user(id)
    user.status = User.status_deleted
    save_user(user)
    return redirect('/retrieveUsers')


@user_controller.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        email = login_form.email.data
        password = login_form.password.data
        user = get_user_for_login(email, password)
        if user is not None:
            session['user_name'] = user.name
            session['user_type'] = user.user_type
            return redirect('/')
        else:
            error = 'Invalid email or password'
            return render_template('login.html', form=login_form, error=error)
    else:
        return render_template('login.html', form=login_form)


@user_controller.route('/logout')
def logout():
    session.pop('user_name', None)
    session.pop('user_type', None)
    return redirect('/')
