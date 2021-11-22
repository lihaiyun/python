from person import Person

person_list = []

# Add person
# for i in range(2):
#     nric = input('Enter NRIC: ')
#     name = input('Enter name: ')
#     p = Person(nric, name)
#     person_list.append(p)

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

# display all person
for p in person_list:
    print(p)

# find person
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
