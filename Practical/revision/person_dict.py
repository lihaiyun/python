from person import Person

person_dict = {}

# Add person
for i in range(2):
    nric = input('Enter NRIC: ')
    name = input('Enter name: ')
    p = Person(nric, name)
    person_dict[nric] = p

# display all person
for p in person_dict.values():
    print(p)

# find person
nric = input('Enter NRIC to find: ')
found = None
if nric in person_dict:
    found = person_dict[nric]
if found is not None:
    print(f'Person found: {found}')
else:
    print('Person not found')
