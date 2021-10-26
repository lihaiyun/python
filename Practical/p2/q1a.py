numList = []

count = int(input('How many numbers do you want to capture? '))
for i in range(count):
    num = int(input(f'Enter number # {i+1}: '))
    numList.append(num)

print()
print(f'The lowest number: {min(numList)}')
print(f'The highest number: {max(numList)}')
print(f'The total of the numbers: {sum(numList)}')
print(f'The average of the numbers: {sum(numList)/len(numList)}')
