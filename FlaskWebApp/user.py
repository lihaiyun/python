class User:
    count = 0

    type_public = 'public'
    type_staff = 'staff'

    status_active = 1
    status_deleted = 0

    def __init__(self, email, password, name):
        User.count += 1
        self.__id = User.count
        self.__email = email
        self.__password = password
        self.__name = name
        self.__type = User.type_public
        self.__status = User.status_active

    def __str__(self):
        return f'ID: {self.__id}\nEmail: {self.__email}\nName: {self.__name}\nType: {self.__type}\nStatus: {self.__status}\n'


user1 = User('user1@test.com', 'flaskwebapp', 'Alice')
print(user1)
user2 = User('user2@test.com', 'flaskwebapp', 'Bryan')
print(user2)
