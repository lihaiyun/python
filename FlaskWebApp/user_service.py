import shelve


def get_user_list():
    user_dict = {}
    db = shelve.open('library')
    if 'users' in db:
        user_dict = db['users']
    db.close()
    return user_dict.values()


def save_user(user):
    user_dict = {}
    db = shelve.open('library')
    if 'users' in db:
        user_dict = db['users']
    user_dict[user.id] = user
    db['users'] = user_dict
    db.close()
