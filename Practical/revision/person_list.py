from person import Person

person_list = []

for i in range(2):
    nric = input('Enter NRIC: ')
    name = input('Enter name: ')
    p = Person(nric, name)
    person_list.append(p)

for p in person_list:
    print(p)
