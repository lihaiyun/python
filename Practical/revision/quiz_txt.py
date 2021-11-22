from fame import Fame

quiz_pool = {'The national athem of Singapore': 'Majulah Singapura',
             'The national flower of Singapore': 'Vanda Miss Joaquim',
             'The national language of Singapore': 'Malay'}


def take_quiz():
    count = 1
    score = 0
    print('Get Read... We are starting the quiz')
    for quest in quiz_pool:
        answer = input(f'{count}. {quest}: ')
        if answer.upper() == quiz_pool[quest].upper():
            score += 1
        count += 1
    print(f'Your score is {score}')
    add = input('Do you want to add your record to Hall of Fame? (y/n) ')
    if add.upper() == 'Y':
        admin_no = input('Enter your admin no: ')
        file = open('fame.txt', 'a')
        file.write(f'{admin_no},{score}\n')
        file.close()


def display_results():
    try:
        file = open('fame.txt', 'r')
        lines = file.readlines()
        fame_list = []
        for line in lines:
            values = line.split(',')
            admin_no = values[0].strip()
            name = values[1].strip()
            fame = Fame(admin_no, name)
            fame_list.append(fame)
        sorted_list = sorted(fame_list, key=by_score, reverse=True)
        for fame in sorted_list:
            print(fame)
    except IOError:
        print('File not existed')


def by_score(fame):
    return fame.score


def main():
    while True:
        print('1. Take the Quiz')
        print('2. Retrieve Hall of Fame')
        print('0. Quit')
        try:
            cmd = int(input('Enter command (1,2,3,0): '))
        except ValueError:
            cmd = 0
        if cmd == 1:
            take_quiz()
        elif cmd == 2:
            display_results()
        else:
            print('End of program')
            break


main()
