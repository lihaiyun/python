class Phone:
    def __init__(self, phone_id, make, model, price):
        self.__id = phone_id
        self.__make = make
        self.__model = model
        self.__price = price

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return f'(id: {self.__id}) {self.__make} {self.__model} at ${self.__price:.2f}'
