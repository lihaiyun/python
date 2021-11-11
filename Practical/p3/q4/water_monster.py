from monster import Monster


class WaterMonster(Monster):
    def __init__(self, name='waterbird'):
        super().__init__(name, 15, 6, 3, 'water')
