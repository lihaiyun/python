class Customer:
    def __init__(self):
        self.__name = None
        self.__email = None
        self.__mobile_number = None

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_mobile_number(self):
        return self.__mobile_number

    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_mobile_number(self, mobile_number):
        self.__mobile_number = mobile_number


name = input('Enter your name: ')
email = input('Enter your email: ')
mobile_number = input('Enter your mobile number: ')

customer = Customer()
customer.set_name(name)
customer.set_email(email)
customer.set_mobile_number(mobile_number)

print(f'Name: {customer.get_name()}')
print(f'Email: {customer.get_email()}')
print(f'Mobile Number: {customer.get_mobile_number()}')
