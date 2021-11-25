import shelve


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
