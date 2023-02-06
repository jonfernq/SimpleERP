# generate_testdates_between.py - 
# with Faker generates n test dates within a date range

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
    return dates
    
start_date = "2023-01-01"
end_date = "2023-01-15"
n = 30
dates = generate_dates(n, start_date, end_date)
print(dates)

