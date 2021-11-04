import uuid


class User:
    type_public = 'public'
    type_staff = 'staff'

    status_active = 1
    status_deleted = 0

    def __init__(self, email, password, name, gender, membership=None, remarks=None):
        self.id = str(uuid.uuid4())
        self.email = email
        self.password = password
        self.name = name
        self.gender = gender
        self.membership = membership
        self.remarks = remarks
        self.type = User.type_public
        self.status = User.status_active

    def __str__(self):
        return f'ID: {self.id}\nEmail: {self.email}\nName: {self.name}\nGender: {self.gender}\n' \
               f'Membership: {self.membership}\nRemarks:{self.remarks}\n' \
               f'Type: {self.type}\nStatus: {self.status}\n'


# user1 = User('user1@test.com', 'flaskwebapp', 'Alice', 'F')
# print(user1)
# user2 = User('user2@test.com', 'flaskwebapp', 'Bryan', 'M')
# print(user2)
