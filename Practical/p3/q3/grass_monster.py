from monster import Monster


class GrassMonser(Monster):
    def __init__(self, name='grasshopper'):
        super().__init__(name, 20, 5, 3, 'grass')
