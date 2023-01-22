import mysql.connector
import csv
from tabular import tabular

# Connect to the database
mydb = mysql.connector.connect(
  host="hostname",
  user="username",
  password="password",
  database="databasename"
)

mycursor = mydb.cursor()

# Retrieve sales performance data from the database
mycursor.execute("SELECT s.name, SUM(sp.amount) as total_sales, sq.amount as sales_quota FROM salespeople s JOIN sales_performance sp ON s.salesperson_id = sp.salesperson_id JOIN sales_quotas sq ON s.salesperson_id = sq.salesperson_id GROUP BY s.salesperson_id")
sales_performance = mycursor.fetchall()

# Create a list of dictionaries with the sales performance data
sales_performance_data = []
for row in sales_performance:
    sales_performance_data.append({
        'name': row[0],
        'total_sales': row[1],
        'sales_quota': row[2],
        'achieved_quota': row[1] >= row[2]
    })

# Sort the sales performance data by total sales
sales_performance_data = sorted(sales_performance_data, key=lambda x: x['total_sales'], reverse=True)

# Create a CSV file with the sales performance data
with open('sales_performance.csv', mode='w') as csv_file:
    fieldnames = ['name', 'total_sales', 'sales_quota', 'achieved_quota']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for data in sales_performance_data:
        writer.writerow(data)

# Create a plain text file with the sales performance data using tabular library
with open('sales_performance.txt', mode='w') as txt_file:
    t = tabular.Tabular()
    t.add_column('Name', [x['name'] for x in sales_performance_data])
    t.add_column('Total Sales', [x['total_sales'] for x in sales_performance_data])
    t.add_column('Sales Quota', [x['sales_quota'] for x in sales_performance_data])
    t.add_column('Achieved Quota', [x['achieved_quota'] for x in sales_performance_data])
    txt_file.write(t.render())

# Close the cursor and the database connection
mycursor.close()
mydb.close()
