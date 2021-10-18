class Phone:
    def __init__(self, make, model, price):
        self.__make = make
        self.__model = model
        self.__price = price

    def get_info(self):
        return f'The price of {self.__make} {self.__model} is ${self.__price}'


make = input('Enter the phone make: ')
model = input('Enter the phone model: ')
price = input('Enter the phone price: ')
phone = Phone(make, model, price)
print(phone.get_info())
