from person import Person

person_list = []


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
            person_list.append(p)
    except:
        print('Error to open file')


# Add person
def add_person():
    for i in range(2):
        nric = input('Enter NRIC: ')
        name = input('Enter name: ')
        p = Person(nric, name)
        person_list.append(p)


# Display all person
def display_all():
    for p in person_list:
        print(p)


# Find person
def find_person():
    nric = input('Enter NRIC to find: ')
    found = None
    for p in person_list:
        if p.nric == nric:
            found = p
            break
    if found is not None:
        print(f'Person found: {found}')
    else:
        print('Person not found')


# Save data to txt
def save_to_txt():
    file = open('person.txt', 'w')
    for p in person_list:
        file.write(f'{p.nric},{p.name}\n')
    file.close()


read_from_txt()
# add_person()
display_all()
# find_person()
save_to_txt()
