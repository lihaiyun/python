class Phone:
    count = 0

    def __init__(self, make, model, price):
        self.__make = make
        self.__model = model
        self.__price = price
        Phone.count += 1

    def get_price(self):
        return self.__price

    def get_info(self):
        return f'{self.__make} {self.__model} at ${self.__price:.2f}'

    def __str__(self):
        return f'The phone created is {self.get_info()}. Now there is {Phone.count} phone in total.'
