class Person:
    def __init__(self, nric, name):
        self.__nric = nric
        self.__name = name

    def __str__(self):
        return f'NRIC: {self.__nric}, Name: {self.__name}'

