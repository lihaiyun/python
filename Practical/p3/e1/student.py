from person import Person


class Student(Person):
    def __init__(self, nric, name, gpa):
        super().__init__(nric, name)
        self.__gpa = gpa

    def __str__(self):
        return f'{super().__str__()}, GPA: {self.__gpa}'
