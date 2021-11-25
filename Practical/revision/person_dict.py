import shelve
from person import Person


# Read data from txt
def read_from_txt():
    data_dict = {}
    try:
        file = open('person.txt', 'r')
        lines = file.readlines()
        for line in lines:
            values = line.split(',')
            nric = values[0].strip()
            name = values[1].strip()
            p = Person(nric, name)
            data_dict[nric] = p
    except IOError:
        print('Error when open file')
    return data_dict


# Read data from shelve
def read_from_shelve():
    data_dict = {}
    try:
        db = shelve.open('storage')
        if 'person' in db:
            data_dict = db['person']
        db.close()
    except:
        print('Error when open shelve')
    return data_dict


# Add person
def add_person():
    nric = input('Enter NRIC: ')
    name = input('Enter name: ')
    p = Person(nric, name)
    person_dict[nric] = p


# Display all person
def display_all():
    for p in person_dict.values():
        print(p)


# Find person
def find_person():
    nric = input('Enter NRIC to find: ')
    if nric in person_dict:
        found = person_dict[nric]
        print(f'Person found: {found}')
    else:
        print('Person not found')


# Save data to txt
def save_to_txt():
    try:
        file = open('person.txt', 'w')
        for p in person_dict.values():
            file.write(f'{p.nric},{p.name}\n')
        file.close()
    except:
        print('Error when write to file')


# Save data to shelve
def save_to_shelve():
    try:
        db = shelve.open('storage')
        db['person'] = person_dict
        db.close()
    except:
        print('Error when open shelve')


# person_dict = read_from_txt()
person_dict = read_from_shelve()
# add_person()
display_all()
# find_person()
# save_to_txt()
save_to_shelve()
