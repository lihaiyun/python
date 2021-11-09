from person import Person

class Lecturer(Person):
    hourly_rate = 90

    def __init__(self, nric, name, teaching_hour):
        super().__init__(nric, name)
        self.__staff_id = nric
        self.__teaching_hour = teaching_hour

    def get_salary(self):
        return self.__teaching_hour * Lecturer.hourly_rate

    def __str__(self):
        return f'Name: {self.get_name()}, Staff Id: {self.__staff_id}, Salary: {self.get_salary()}'
