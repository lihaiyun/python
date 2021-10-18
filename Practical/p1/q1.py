class Customer:
    def __init__(self, name, email, mobile_number):
        self.__name = name
        self.__email = email
        self.__mobile_number = mobile_number

    def get_info(self):
        return f'Name: {self.__name}, Email: {self.__email}, Mobile Number: {self.__mobile_number}'


customer = Customer('Haiyun', 'haiyun@gmail.com', 98765432)
print(customer.get_info())
