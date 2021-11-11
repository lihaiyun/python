from fire_monster import FireMonster
from water_monster import WaterMonster
from grass_monster import GrassMonser
import random

player_monster = None
type = input('Choose your monster type (F, W or G): ')
if type.upper() == 'F':
    player_monster = FireMonster()
elif type.upper() == 'W':
    player_monster = WaterMonster()
elif type.upper() == 'G':
    player_monster = GrassMonser()
else:
    exit('Invalid monster type')
name = input('Enter your monster name: ')
if len(name.strip()) > 0:
    player_monster.name = name
print(f'Your monster is {player_monster.name}')

num = random.randint(0, 2)
if num == 0:
    computer_monster = FireMonster()
elif num == 1:
    computer_monster = WaterMonster()
else:
    computer_monster = GrassMonser()
print(f'Enemy monster is {computer_monster.name}')

print('Game starts. You attack enemy first.')
while True:
    damage = player_monster.attack - computer_monster.defence
    computer_monster.receive_damage(damage)
    print(f'Enemy monster {computer_monster.name} suffers {damage} damage, health is {computer_monster.health} now')
    if computer_monster.health == 0:
        print('You Win!')
        break

    damage = computer_monster.attack - player_monster.defence
    player_monster.receive_damage(damage)
    print(f'Your monster {player_monster.name} suffers {damage} damage, health is {player_monster.health} now')
    if player_monster.health == 0:
        print('You Lose!')
        break
