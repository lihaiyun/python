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
        if num is not None and num > 0:
            num_list.append(num)
            break
print(f'Sum is {sum(num_list)}')
