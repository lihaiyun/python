import uuid
from datetime import datetime
from constants import date_format, datetime_format


class User:
    gender_dict = {
        '': 'Select', 'F': 'Female', 'M': 'Male'
    }
    membership_dict = {
        'F': 'Fellow', 'S': 'Senior', 'P': 'Professional'
    }
    user_type_dict = {
        'C': 'Customer', 'S': 'Staff'
    }

    status_active = 1
    status_deleted = 0

    def __init__(self, email, password, name, gender, membership, remarks=None, birthday=None, user_type='C'):
        self.id = str(uuid.uuid4())
        self.email = email
        self.password = password
        self.name = name
        self.gender = gender
        self.membership = membership
        self.remarks = remarks
        self.birthday = birthday
        self.user_type = user_type
        self.status = User.status_active
        self.time_created = datetime.now()
        self.time_updated = datetime.now()

    def get_gender_str(self):
        return User.gender_dict[self.gender]

    def get_membership_str(self):
        return User.membership_dict[self.membership]

    def get_user_type_str(self):
        return User.user_type_dict[self.user_type]

    def get_birthday_str(self):
        if self.birthday is None:
            return 'Unknown'
        else:
            return self.birthday.strftime(date_format)

    def get_time_created_str(self):
        return self.time_created.strftime(datetime_format)

    def get_time_updated_str(self):
        return self.time_updated.strftime(datetime_format)

    def __str__(self):
        return f'ID: {self.id}\n' \
               f'Email: {self.email}\n' \
               f'Name: {self.name}\n' \
               f'Gender: {self.get_gender_str()}\n' \
               f'Birthday: {self.get_birthday_str()}\n' \
               f'Membership: {self.get_membership_str()}\n' \
               f'Remarks: {self.remarks}\n' \
               f'User Type: {self.get_user_type_str()}\n' \
               f'Status: {self.status}\n' \
               f'Date Created: {self.get_time_created_str()}\n' \
               f'Date Updated: {self.get_time_updated_str()}\n'


# user1 = User('user1@test.com', 'FlaskWebapp', 'Alice', 'F', 'F')
# print(user1)
# user2 = User('user2@test.com', 'FlaskWebapp', 'Bryan', 'M', 'P', 'I love python',
#              datetime.strptime('15/05/2005', date_format), 'S')
# print(user2)
