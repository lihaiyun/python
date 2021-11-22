class Person:
    def __init__(self, nric, name):
        self.nric = nric
        self.name = name

    def __str__(self):
        return f'NRIC: {self.nric}, Name: {self.name}'
