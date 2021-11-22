from person import Person

person_list = []

# Add person
for i in range(2):
    nric = input('Enter NRIC: ')
    name = input('Enter name: ')
    p = Person(nric, name)
    person_list.append(p)

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
