import shelve
from person import Person

person_dict = {}


# Read data from txt
def read_from_txt():
    try:
        file = open('person.txt', 'r')
        lines = file.readlines()
        for line in lines:
            values = line.split(',')
            nric = values[0].strip()
            name = values[1].strip()
            p = Person(nric, name)
            person_dict[nric] = p
    except:
        print('Error to open file')


# Read data from shelve
def read_from_shelve():
    db = shelve.open('storage')
    if 'person' in db:
        person_dict = db['person']


# Add person
def add_person():
    for i in range(2):
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


# Save data to shelve
def save_to_shelve():
    db = shelve.open('storage')
    db['person'] = person_dict
    db.close()


read_from_txt()
# add_person()
display_all()
# find_person()
save_to_shelve()
