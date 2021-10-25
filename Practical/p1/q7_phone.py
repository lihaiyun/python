class Phone:
    count = 0

    def __init__(self, make, model, price):
        Phone.count += 1
        self.__id = Phone.count
        self.__make = make
        self.__model = model
        self.__price = price

    def get_id(self):
        return self.__id

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return f'(id: {self.__id}) {self.__make} {self.__model} at ${self.__price:.2f}'
