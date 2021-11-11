from monster import Monster


class FireMonster(Monster):
    def __init__(self, name):
        super().__init__(name, 10, 9, 4, 'fire')
