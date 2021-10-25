from q7_phone import Phone

phones = {}


def get_phone(phone_id):
    if phone_id in phones:
        phone = phones[phone_id]
        return phone
    else:
        return None


def display_all():
    if len(phones) > 0:
        for phone_id in phones:
            print(phones[phone_id])
    else:
        print('There is no phone')


def search():
    phone_id = int(input('Enter phone id to search: '))
    phone = get_phone(phone_id)
    if phone is not None:
        print(phone)
    else:
        print('Phone not found')


def add():
    make = input('Enter the phone make: ')
    model = input('Enter the phone model: ')
    price = input('Enter the phone price: ')
    phone = Phone(make, model, float(price))
    phones[phone.get_id()] = phone
    print(f'The phone is added: {phone}')


def update():
    phone_id = int(input('Enter phone id to update: '))
    phone = get_phone(phone_id)
    if phone is not None:
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
    phone_id = int(input('Enter phone id to delete: '))
    phone = get_phone(phone_id)
    if phone is not None:
        del phones[phone_id]
        print(f'The phone is deleted: {phone}')
    else:
        print('Phone not found')


def display_menu():
    print('--------------------------')
    print('Phone Management System')
    print('0 - Display all')
    print('1 - Search')
    print('2 - Add')
    print('3 - Update')
    print('4 - Delete')
    print('5 - Quit')
    command = int(input('Enter the command (1-5): '))
    return command


while True:
    command = display_menu()
    if command == 0:
        display_all()
    if command == 1:
        search()
    elif command == 2:
        add()
    elif command == 3:
        update()
    elif command == 4:
        delete()
    elif command == 5:
        print('Bye')
        break
    print()
