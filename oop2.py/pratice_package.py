from classorder.customer import Customer
from classorder.order import Order

jame = Customer('Jame','Nonthaburi')
ord_jame = Order('15-06-2022','Packed')

print(f'Order of {jame.name} on {ord_jame.date} is {ord_jame.status}')

