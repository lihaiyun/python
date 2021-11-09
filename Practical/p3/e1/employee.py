from person import Person

class Employee(Person):
    def __init__(self, nric, name, salary):
        super().__init__(nric, name)
        self.__salary = salary

    def __str__(self):
        return f'{super().__str__()}, Salary: {self.__salary}'
