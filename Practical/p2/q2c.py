try:
    file = open('bmi.txt', 'r')
    lines = file.readlines()
    count = 0
    for line in lines:
        count += 1
        print(f'Line #{count}: {line.strip()}')
    file.close()
except IOError:
    print('Error when open file')
