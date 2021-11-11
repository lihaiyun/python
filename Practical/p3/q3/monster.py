class Monster:
    def __init__(self, name, health, attack, defence, type=None):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence
        self.type = type

    def __str__(self):
        return f'{self.name} is {self.type} type monster'
