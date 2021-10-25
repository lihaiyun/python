class SalesPerson:
    commission_rate = 0.2

    def __init__(self, name):
        self.__name = name
        self.__commission = 0

    def set_commission(self, payment):
        self.__commission = payment * SalesPerson.commission_rate

    def __str__(self):
        return f'The commission of salesperson {self.__name} is ${self.__commission:.2f}'


name = input('Enter salesperson name: ')
payment = float(input('Enter payment received: '))
salesperson = SalesPerson(name)
salesperson.set_commission(payment)
print(salesperson)
