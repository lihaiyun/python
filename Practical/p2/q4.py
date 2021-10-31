from phone import Phone
import shelve

phone_dict = {}


def search():
    phone_id = input('Enter phone id to search: ')
    if phone_id in phone_dict:
        phone = phone_dict[phone_id]
        print(phone)
    else:
        print('Phone not found')


def add():
    phone_id = input('Enter the phone id: ')
    if phone_id not in phone_dict:
        make = input('Enter the phone make: ')
        model = input('Enter the phone model: ')
        price = input('Enter the phone price: ')
        phone = Phone(phone_id, make, model, float(price))
        phone_dict[phone_id] = phone
        print(f'The phone is added: {phone}')
    else:
        print('Phone id already exists')


def update():
    phone_id = input('Enter phone id to update: ')
    if phone_id in phone_dict:
        phone = phone_dict[phone_id]
        make = input('Enter the new make (leave empty to remain unchanged): ')
        model = input('Enter the new model (leave empty to remain unchanged): ')
        price = input('Enter the new price (leave empty to remain unchanged): ')
        if len(make) > 0:
            phone.set_make(make)
        if len(model) > 0:
            phone.set_model(model)
        if len(price) > 0:
            phone.set_price(float(price))
        print(f'The phone is updated: {phone}')
    else:
        print('Phone not found')


def delete():
    phone_id = input('Enter phone id to delete: ')
    if phone_id in phone_dict:
        phone = phone_dict[phone_id]
        del phone_dict[phone_id]
        print(f'The phone is deleted: {phone}')
    else:
        print('Phone not found')


def display_all():
    if len(phone_dict) > 0:
        for phone_id in phone_dict:
            print(phone_dict[phone_id])
    else:
        print('No phone available')


def display_menu():
    print('--------------------------')
    print('Phone Management System')
    print('1 - Search')
    print('2 - Add')
    print('3 - Update')
    print('4 - Delete')
    print('5 - Display all')
    print('6 - Quit')
    command = int(input('Enter the command (1-5): '))
    return command


try:
    db = shelve.open('inventory')
    if 'phones' in db:
        phone_dict = db['phones']
except:
    exit('Error when get data from shelve')

while True:
    command = display_menu()
    if command == 1:
        search()
    elif command == 2:
        add()
    elif command == 3:
        update()
    elif command == 4:
        delete()
    elif command == 5:
        display_all()
    elif command == 6:
        db['phones'] = phone_dict
        db.close()
        print('Bye')
        break
    print()
