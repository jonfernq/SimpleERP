import random
from faker import Faker
fake = Faker()

# Create a list of employees
employees = []
for i in range(5):
    first_name = fake.first_name()
    last_name = fake.last_name()
    address = fake.address()
    phone = fake.phone_number()
    email = fake.email()
    ssn = fake.ssn()
    hire_date = fake.date_between(start_date="-1y", end_date="today")
    salary = round(random.uniform(3000, 20000), 2)
    tax_rate = round(random.uniform(0.1, 0.3), 2)
    employees.append((first_name, last_name, address, phone, email, ssn, hire_date, salary, tax_rate))

# Create a list of payrolls
payrolls = []
for i in range(20):
    employee_id = random.randint(1, len(employees))
    pay_period_start = fake.date_between(start_date="-1y", end_date="

    pay_period_end = fake.date_between(start_date=pay_period_start, end_date="+1m")
    hours_worked = round(random.uniform(20, 80), 2)
    gross_pay = round(hours_worked * salary / 2080, 2)
    deductions = round(gross_pay * tax_rate, 2)
    net_pay = gross_pay - deductions
    payrolls.append((employee_id, pay_period_start, pay_period_end, hours_worked, gross_pay, deductions, net_pay))

# Create a list of deductions
deductions = []
deduction_types = ["Federal Tax", "State Tax", "Social Security", "Medicare", "Health Insurance"]
for i in range(20):
    employee_id = random.randint(1, len(employees))
    deduction_type = random.choice(deduction_types)
    amount = round(random.uniform(20, 500), 2)
    deductions.append((employee_id, deduction_type, amount))

# Create a list of timeclock entries
timeclock = []
for i in range(20):
    employee_id = random.randint(1, len(employees))
    clock_in = fake.date_time_between(start_date="-1y", end_date="now"
    clock_out = fake.date_time_between(start_date=clock_in, end_date="+8h")
    timeclock.append((employee_id, clock_in, clock_out))

# Open the file to write the SQL statements
with open("insert_data.sql", "w") as file:
    # Write SQL INSERT statements for employees
    for employee in employees:
        file.write(f"INSERT INTO Employee (FirstName, LastName, Address, Phone, Email, SocialSecurityNumber, HireDate, Salary, TaxRate) VALUES ('{employee[0]}', '{employee[1]}', '{employee[2]}', '{employee[3]}', '{employee[4]}', '{employee[5]}', '{employee[6]}', {employee[7]}, {employee[8]});\n")

    # Write SQL INSERT statements for payrolls
    for payroll in payrolls:
        file.write(f"INSERT INTO Payroll (EmployeeID, PayPeriodStart, PayPeriodEnd, HoursWorked, GrossPay, Deductions, NetPay) VALUES ({payroll[0]}, '{payroll[1]}', '{payroll[2]}', {payroll[3]}, {payroll[4]}, {payroll[5]}, {payroll[6]});\n")

    # Write SQL INSERT statements for deductions
    for ded in deductions:
        file.write(f"INSERT INTO Deduction (EmployeeID, DeductionType, Amount) VALUES ({ded[0]}, '{ded[1]}', {ded[2]});\n")

    # Write SQL INSERT statements for timeclock
    for clock in timeclock:
        file.write(f"INSERT INTO Timeclock (EmployeeID, ClockIn, ClockOut) VALUES ({clock[0]}, '{clock[1]}', '{clock[2]}');\n")

# Close the database connection
conn.close()

