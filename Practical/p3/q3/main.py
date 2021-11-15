from monster import Monster
from fire_monster import FireMonster
from water_monster import WaterMonster
from grass_monster import GrassMonser

m1 = FireMonster('charmander')
m2 = WaterMonster('squirtle')
m3 = GrassMonser('bulbasaur')

# print(m1)
# print(m2)
# print(m3)


def display_info(monster):
    if isinstance(monster, Monster):
        print(monster)
    else:
        print('Invalid monster')


display_info(m1)
display_info(m2)
display_info(m3)
display_info('Test')
