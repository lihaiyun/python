import shelve
from datetime import datetime
from user import User

db_name = 'library'
db_users_key = 'users'


def check_status(user):
    return user.status > 0


def by_time_updated(user):
    return user.time_updated


def get_user_list():
    user_dict = {}
    db = shelve.open(db_name)
    if db_users_key in db:
        user_dict = db[db_users_key]
    db.close()
    user_list = user_dict.values()
    user_list = filter(check_status, user_list)
    user_list = sorted(user_list, key=by_time_updated, reverse=True)
    return user_list


def get_user(id):
    result = None
    user_dict = {}
    db = shelve.open(db_name)
    if db_users_key in db:
        user_dict = db[db_users_key]
    db.close()
    if id in user_dict:
        result = user_dict[id]
    return result


def get_user_for_login(email, password):
    result = None
    user_dict = {}
    db = shelve.open(db_name)
    if db_users_key in db:
        user_dict = db[db_users_key]
    db.close()
    for user in user_dict.values():
        if user.email == email and \
                user.password == password and \
                user.status == User.status_active:
            result = user
    return result


def save_user(user):
    user.time_updated = datetime.now()
    user_dict = {}
    db = shelve.open(db_name)
    if db_users_key in db:
        user_dict = db[db_users_key]
    user_dict[user.id] = user
    db[db_users_key] = user_dict
    db.close()
