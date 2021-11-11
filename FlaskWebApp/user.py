import uuid
from datetime import datetime


class User:
    type_customer = 'customer'
    type_staff = 'staff'

    status_active = 1
    status_deleted = 0

    date_format = '%d/%m/%Y'
    datetime_format = '%d/%m/%Y %H:%M:%S'

    def __init__(self, email, password, name, gender, membership=None, remarks=None, birthday=None):
        self.id = str(uuid.uuid4())
        self.email = email
        self.password = password
        self.name = name
        self.gender = gender
        self.membership = membership
        self.remarks = remarks
        self.birthay = birthday
        self.type = User.type_customer
        self.status = User.status_active
        self.time_created = datetime.now()
        self.time_updated = datetime.now()

    def get_birthday_str(self):
        if self.birthay is None:
            return 'Unknown'
        else:
            return self.birthay.strftime(User.date_format)

    def get_time_created_str(self):
        return self.time_created.strftime(User.datetime_format)

    def get_time_updated_str(self):
        return self.time_updated.strftime(User.datetime_format)

    def __str__(self):
        return f'ID: {self.id}\nEmail: {self.email}\nName: {self.name}\nGender: {self.gender}\n' \
               f'Birthday: {self.get_birthday_str()}\n' \
               f'Membership: {self.membership}\nRemarks: {self.remarks}\n' \
               f'Type: {self.type}\nStatus: {self.status}\n' \
               f'Date Created: {self.get_time_created_str()}\n' \
               f'Date Updated: {self.get_time_updated_str()}\n'


# user1 = User('user1@test.com', 'flaskwebapp', 'Alice', 'F')
# print(user1)
# user2 = User('user2@test.com', 'flaskwebapp', 'Bryan', 'M')
# print(user2)
