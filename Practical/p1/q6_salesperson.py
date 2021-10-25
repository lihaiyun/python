class SalesPerson:
    commission_rate = 0.2

    def __init__(self, name):
        self.__name = name
        self.__phone = None
        self.__commission = 0

    def sold(self, phone):
        self.__phone = phone
        self.__commission = phone.get_price() * SalesPerson.commission_rate

    def __str__(self):
        return f'Salesperson {self.__name} sold {self.__phone.get_info()} and earned commission of ${self.__commission:.2f}.'
