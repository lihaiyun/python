import shelve
from person import Person


# Read data from txt
def read_from_txt():
    dict = {}
    try:
        file = open('person.txt', 'r')
        lines = file.readlines()
        for line in lines:
            values = line.split(',')
            nric = values[0].strip()
            name = values[1].strip()
            p = Person(nric, name)
            dict[nric] = p
    except:
        print('Error to open file')
    return dict


# Read data from shelve
def read_from_shelve():
    dict = {}
    db = shelve.open('storage')
    if 'person' in db:
        dict = db['person']
    return dict


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
    found = None
    if nric in person_dict:
        found = person_dict[nric]
    if found is not None:
        print(f'Person found: {found}')
    else:
        print('Person not found')


# Save data to txt
def save_to_txt():
    file = open('person.txt', 'w')
    for p in person_dict.values():
        file.write(f'{p.nric},{p.name}\n')
    file.close()


# Save data to shelve
def save_to_shelve():
    db = shelve.open('storage')
    db['person'] = person_dict
    db.close()


# person_dict = read_from_txt()
person_dict = read_from_shelve()
# add_person()
display_all()
# find_person()
# save_to_txt()
save_to_shelve()
