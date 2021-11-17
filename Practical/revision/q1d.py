def get_num(str):
    try:
        num = int(str)
        return num
    except:
        return None


num_list = []
for i in range(3):
    while True:
        num_str = input(f'Enter integer {i+1}: ')
        num = get_num(num_str)
        if num is not None and 1 <= num <= 100:
            num_list.append(num)
            break
        else:
            print('The number must be between 1 and 100. Please try again.')
print(f'Sum is {sum(num_list)}')
