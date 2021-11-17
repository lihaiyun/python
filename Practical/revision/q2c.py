from list import read_input, search

num_list = read_input()
print(num_list)
num = int(input('Enter a number to search: '))
result = search(num_list, num)
if result:
    print(f'Number {num} found')
else:
    print(f'Number {num} not found')
print('End of program')
