from person import Person

person_dict = {}

for i in range(2):
    nric = input('Enter NRIC: ')
    name = input('Enter name: ')
    p = Person(nric, name)
    person_dict[nric] = p

for p in person_dict.values():
    print(p)
