## Expense Management
When the finance or accounting department processes employee expense reports in a small company, the typical business processes that are part of this include:
1.  Review and verify: Reviewing and verifying expense reports for compliance with company policies and guidelines
2.  Reimburse or pay: Processing employee reimbursements and/or payments for expenses
3.  Record and track: Recording and tracking expenses in the company's financial system or accounting software
4.  Audit and reconcile: Auditing and reconciling expenses with credit card statements or receipts
5.  Analyze and report:  Generating reports and analysis of expense data to identify trends or areas for cost savings
6.  Communicate and educate: Communicating with employees and managers regarding expense policies and procedures.
### DB Tables

![expense-management](https://user-images.githubusercontent.com/68504324/213844629-0eaa8b18-2292-4e4b-b2f3-089e55bdc8bf.png)

DB tables are described by SQL Create statements in the [em-create-tables.sql](https://github.com/jonfernq/SimpleERP/blob/main/Expense-Management/em-create-tables.sql) file.

### Test Data 
Realistic test is created by [em-test-data.py](https://github.com/jonfernq/SimpleERP/blob/main/Expense-Management/em-test-data.py), consisting of SQL Insert statements in the [expense-management-data.sql](https://github.com/jonfernq/SimpleERP/blob/main/Expense-Management/expense-management-data.sql) file.

### Reporting
An employee expense management system such as the one described above can produce a variety of reports, some examples include:

1.  [Expense Report by Employee](https://github.com/jonfernq/SimpleERP/blob/main/Expense-Management/expense-report-by-employee.py): This report shows the total expenses incurred by each employee, as well as a breakdown of expenses by category.
2.  Expense Report by Category: This report shows the total expenses incurred for each category, as well as a breakdown of expenses by employee.
3.  Expense Report by Date: This report shows the total expenses incurred for a specific date range, as well as a breakdown of expenses by employee and category.
4.  Out of Policy Report: This report shows all expenses that were incurred that do not comply with the company's expense policy.
5.  Reimbursement Report: This report shows all the reimbursements done to employees for the expenses they incurred.
6.  Credit Card Report: This report shows all expenses that were charged to a company credit card, as well as a breakdown of expenses by employee and category.
7.  Budget vs Actual Report: This report compares the budgeted expenses with the actual expenses incurred, highlighting any variances.
8.  Audit Report: This report shows the details of expenses that were audited and the outcome of the audit.
    
