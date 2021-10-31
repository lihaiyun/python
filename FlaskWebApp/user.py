import uuid


class User:
    type_public = 'public'
    type_staff = 'staff'

    status_active = 1
    status_deleted = 0

    def __init__(self, email, password, name):
        self.id = uuid.uuid4()
        self.email = email
        self.password = password
        self.name = name
        self.type = User.type_public
        self.status = User.status_active

    def __str__(self):
        return f'ID: {self.id}\nEmail: {self.email}\nName: {self.name}\nType: {self.type}\nStatus: {self.status}\n'


user1 = User('user1@test.com', 'flaskwebapp', 'Alice')
print(user1)
user2 = User('user2@test.com', 'flaskwebapp', 'Bryan')
print(user2)
