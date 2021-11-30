import shelve
from datetime import datetime

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
    user = None
    user_dict = {}
    db = shelve.open(db_name)
    if db_users_key in db:
        user_dict = db[db_users_key]
    if id in user_dict:
        user = user_dict[id]
    db.close()
    return user


def save_user(user):
    user.time_updated = datetime.now()
    user_dict = {}
    db = shelve.open(db_name)
    if db_users_key in db:
        user_dict = db[db_users_key]
    user_dict[user.id] = user
    db[db_users_key] = user_dict
    db.close()
