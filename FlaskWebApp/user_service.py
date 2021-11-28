import shelve

db_name = 'library'
users_key = 'users'


def get_user_list():
    user_dict = {}
    db = shelve.open(db_name)
    if users_key in db:
        user_dict = db[users_key]
    db.close()
    return user_dict.values()


def save_user(user):
    user_dict = {}
    db = shelve.open(db_name)
    if users_key in db:
        user_dict = db[users_key]
    user_dict[user.id] = user
    db[users_key] = user_dict
    db.close()
