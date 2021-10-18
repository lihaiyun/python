class Phone:
    def __init__(self):
        self.__make = None
        self.__model = None
        self.__price = 0

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_price(self, price):
        if price.isnumeric():
            self.__price = price
            return True
        else:
            return False

    def get_info(self):
        return f'The price of {self.__make} {self.__model} is ${self.__price}'


make = input('Enter the phone make: ')
model = input('Enter the phone model: ')
price = input('Enter the phone price: ')

phone = Phone()
phone.set_make(make)
phone.set_model(model)
success = phone.set_price(price)
if not success:
    exit('Price should be in number')

print(phone.get_info())
