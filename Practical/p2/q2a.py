while True:
    name = input('Enter name: ')
    weight = float(input('Enter weight (kg): '))
    height = float(input('Enter height (m): '))

    bmi = weight/height**2
    print(f'{bmi:.2f}')

    command = input('Store your bmi to file? (Y/N): ')
    if command.upper() == 'Y':
        file = open('bmi.txt', 'a')
        file.write(f'{name},{bmi:.2f}\n')
        file.close()

    command = input('Do you want to continue? (Y/N): ')
    if command.upper() == 'N':
        break

command = input('Do you want to view records in file? (Y/): ')
if command.upper() == 'Y':
    file = open('bmi.txt', 'r')
    content = file.read()
    print(content)
    file.close()
