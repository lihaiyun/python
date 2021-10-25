from q6_phone import Phone
from q6_salesperson import SalesPerson

make = input('Enter the phone make: ')
model = input('Enter the phone model: ')
price = float(input('Enter the phone price: '))
phone = Phone(make, model, price)
print(phone)

name = input('Enter salesperson name: ')
salesperson = SalesPerson(name)
salesperson.sold(phone)
print(salesperson)
