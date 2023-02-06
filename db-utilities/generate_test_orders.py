# generate_test_orders.py - 
# then generates a test order with a few order items 
# with a random product id, quantity, and price 
# first Faker generates n test dates within a date range
# todo: Poisson distribution to generate orders based on time of day patterns 

from faker import Faker
import random
import datetime
    
def convert_to_datetime(date_string):
    return datetime.datetime.strptime(date_string, "%Y-%m-%d")

def generate_dates(n, start_date, end_date):
    fake = Faker()
    dates = []
    for i in range(n):
        from_date = convert_to_datetime(start_date) 
        to_date = convert_to_datetime(end_date)  
        fake_date = fake.date_between(start_date=from_date, end_date=to_date)        
        dates.append(fake_date.strftime("%Y-%m-%d"))  
        #print(from_date, to_date, fake.date_between(start_date=from_date, end_date=to_date)) 
        #print('fake_date: ', fake_date)         
    return dates
    
def generate_test_order(order_date): 
    fake = Faker()
    
    order = {
        'OrderID': 'O' + str(random.randint(100000, 999999)),
        'CustomerID': 'C' + str(random.randint(100000, 999999)),
        'OrderDate': order_date,
        'ShippingAddress': fake.address(),
        'TotalCost': round(random.uniform(0, 50), 2)
    }

    order_items = []
    for i in range(random.randint(1, 5)):
        order_item = {
            'OrderItemID': i,
            'OrderID': order['OrderID'],
            'ProductID': 'P' + str(random.randint(100000, 999999)),
            'Quantity': random.randint(1, 10),
            'Price': round(random.uniform(0, 1000), 2)
        }
        order_items.append(order_item)

    return (order, order_items)
    
start_date = "2023-01-01"
end_date = "2023-01-15"
n = 30
dates = generate_dates(n, start_date, end_date)
print(dates)

test_orders = list(map(generate_test_order, dates))
for test_order in test_orders: 
    print(test_order, '\n') 
    

