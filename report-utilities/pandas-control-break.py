
# pandas_control_break.py -  
# emulating typical COBOL business data processing report 


import pandas as pd

# Load sample data into a Pandas DataFrame
data = {'Customer': ['A', 'B', 'A', 'C', 'B', 'C'],
        'Product': ['P1', 'P2', 'P1', 'P2', 'P1', 'P2'],
        'Sales': [100, 200, 150, 300, 175, 250]}
df = pd.DataFrame(data)

# Group the data by Customer and Product
grouped = df.groupby(['Customer', 'Product'])

# Calculate the sum of Sales for each group
report = grouped['Sales'].sum().reset_index()

# Group the report by Customer and calculate the sum of Sales for each customer
customer_totals = report.groupby('Customer')['Sales'].sum().reset_index()
customer_totals.rename(columns={'Sales': 'Customer Total'}, inplace=True)

# Merge the customer totals back into the report
report = pd.merge(report, customer_totals, on='Customer')

# Find the rows in the report where the customer changes
customer_break_rows = report['Customer'].ne(report['Customer'].shift()).cumsum()

# Create a new DataFrame to store the final report
final_report = pd.DataFrame(columns=['Customer', 'Product', 'Sales', 'Customer Total'])

# Loop through each customer in the report
for customer_group, group in report.groupby(customer_break_rows):
    # Add the rows for the current customer to the final report
    final_report = pd.concat([final_report, group], ignore_index=True)
    # Add a row for the customer total after the last row for the current customer
    customer_total = pd.DataFrame({'Customer': '', 'Product': 'Customer Total', 'Sales': group['Sales'].sum(), 'Customer Total': ''}, index=[len(group)])
    final_report = pd.concat([final_report, customer_total], ignore_index=True)

# Add a row containing the grand total at the end of the report
grand_total = pd.DataFrame({'Customer': 'Grand Total', 'Product': '', 'Sales': report['Sales'].sum(), 'Customer Total': report['Customer Total'].sum()}, index=[len(final_report)])
final_report = pd.concat([final_report, grand_total], ignore_index=True)

# Print the final report with customer sub-totals and a grand total
print(final_report)

"""

      Customer         Product Sales Customer Total
0            A              P1   250            250
1               Customer Total   250
2            B              P1   175            375
3            B              P2   200            375
4               Customer Total   375
5            C              P2   550            550
6               Customer Total   550
7  Grand Total                  1175           1550

"""
