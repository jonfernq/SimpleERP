import random
from faker import Faker
fake = Faker()

# Create a list of employees
employees = []
for i in range(5):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    employees.append((first_name, last_name, email))

# Create a list of categories
categories = ["Travel", "Meals", "Office Supplies", "Other"]

# Create a list of expenses
expenses = []
for i in range(20):
    employee_id = random.randint(1, len(employees))
    date = fake.date_between(start_date="-1y", end_date="today")
    description = fake.sentence()
    amount = round(random.uniform(20, 500), 2)
    expenses.append((employee_id, date, description, amount))

# Create a list of expense categories
expense_categories = []
for i in range(20):
    expense_id = i + 1
    category = random.choice(categories)
    expense_categories.append((expense_id, category))

# Create a list of receipts
receipts = []
for i in range(20):
    expense_id = i + 1
    image = fake.image_url()
    receipts.append((expense_id, image))

# Open the file to write the SQL statements
with open("expense_management_data.sql", "w") as file:
    # Write SQL INSERT statements for employees
    for employee in employees:
        file.write(f"INSERT INTO Employee (FirstName, LastName, Email) VALUES ('{employee[0]}', '{employee[1]}', '{employee[2]}');\n")

    # Write SQL INSERT statements for expenses
    for expense in expenses:
        file.write(f"INSERT INTO Expense (EmployeeID, Date, Description, Amount) VALUES ({expense[0]}, '{expense[1]}', '{expense[2]}', {expense[3]});\n")

    # Write SQL INSERT statements for expense categories
    for expense_category in expense_categories:
        file.write(f"INSERT INTO ExpenseCategory (ExpenseID, Category) VALUES ({expense_category[0]}, '{expense_category[1]}');\n")

    # Write SQL INSERT statements for receipts
    for receipt in receipts:
        file.write(f"INSERT INTO Receipt (ExpenseID, Image) VALUES ({receipt[0]}, '{receipt[1]}');\n")
