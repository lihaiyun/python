from person import Person

class Student(Person):
    def __init__(self, nric, name, admin_no, test_mark, exam_mark):
        super().__init__(nric, name)
        self.__admin_no = admin_no
        self.__test_mark = test_mark
        self.__exam_mark = exam_mark

    def get_final_mark(self):
        return (self.__test_mark + self.__exam_mark) / 2

    def __str__(self):
        return f'Name: {self.get_name()}, Admin No: {self.__admin_no}, Final Mark: {self.get_final_mark()}'
