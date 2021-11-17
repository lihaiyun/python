num_list = []
for i in range(3):
    num = int(input(f'Enter integer {i+1}: '))
    num_list.append(num)
print(f'Sum is {sum(num_list)}')
