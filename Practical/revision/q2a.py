def get_num(str):
    try:
        num = int(str)
        return num
    except:
        return None


def read_input():
    num_list = []
    for i in range(10):
        num_str = input('Enter a number: ')
        num = get_num(num_str)
        if num is not None:
            num_list.append(num)
    return num_list


num_list = read_input()
print(num_list)
print('End of program')
