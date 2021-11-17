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


def search(num_list, num):
    return num in num_list
