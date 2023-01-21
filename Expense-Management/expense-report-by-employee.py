import tabular as tb
import csv
import sqlite3

# Connect to the database
conn = sqlite3.connect('expense_management.db')
cursor = conn.cursor()

# Fetch the data from the Expense and Employee tables
cursor.execute("""
SELECT Employee.FirstName, Employee.LastName, SUM(Expense.Amount) as TotalExpenses 
FROM Expense
JOIN Employee ON Expense.EmployeeID = Employee.EmployeeID
GROUP BY Employee.EmployeeID
ORDER BY TotalExpenses DESC
""")
rows = cursor.fetchall()

# Create a tabular report
data = [["Employee", "Expenses"]]
total_expenses = 0
for row in rows:
    data.append([row[0] + " " + row[1], row[2]])
    total_expenses += row[2]
data.append(["Total", total_expenses])

# Write the report to a plain text file
with open("expense_report_by_employee.txt", "w") as file:
    file.write(tb.tabular(data))

# Write the report to a CSV file
with open("expense_report_by_employee.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)

# Close the database connection
conn.close()

/* 

This program connects to a SQLite database named "expense_management.db" using the sqlite3 library and use the execute() method to fetch the data from the Expense and Employee tables, the data fetched is used to create a tabular report using the tabular package that shows the total expenses incurred by each employee, as well as a grand total for all employees.

The program then writes the report to a plain text file using the write() method. The tb.tabular(data) function formats the data in a tabular format and writes it to the file.

It also writes the report to a CSV file using the csv library, with the writerows() method which writes each row of data in the report to the CSV file.

Please note that you need to have tabular package installed in your environment for the above code to work, you can install the package by running !pip install tabular on your command prompt.
You also need to have a database named expense_management.db with Expense and Employee table having the data, you can use the SQL insert statements generated earlier to insert data into the tables.

*/ 
