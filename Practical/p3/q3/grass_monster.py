from monster import Monster


class GrassMonser(Monster):
    def __init__(self, name):
        super().__init__(name, 20, 5, 3, 'grass')
