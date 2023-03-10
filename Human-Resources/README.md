
## Human Resources Management System

A human resources management system for a small company typically performs a variety of business processes, including:

- **Employee information management:** storing and maintaining employee personal and professional information, such as contact details, job titles, and salary information.

- **Recruiting and hiring:** posting job listings, tracking resumes and applications, scheduling interviews, and managing the hiring process.

- **Time and attendance tracking:** keeping track of when employees arrive and leave, calculating hours worked, and generating paychecks.

- **Benefits administration:** managing employee benefits such as health insurance, retirement plans, and paid time off.

- **Performance management:** setting goals, providing feedback, and conducting performance evaluations to assess employee productivity and identify areas for improvement.

- **Compliance:** ensuring compliance with legal and regulatory requirements related to employment, such as compliance with labor laws and equal opportunity laws.

- **Training and development:** tracking employee training and development activities and ensuring that employees have the necessary skills to perform their jobs.

- **Employee self-service:** providing employees with a secure portal to access their personal and professional information, request time off, and manage their benefits.

### HR DB Tables

![hr_plantuml](https://user-images.githubusercontent.com/68504324/212562155-5261f4c5-3e41-47bc-8a20-dd8aab5ece6b.jpg)

HR DB tables are described by SQL Create statements in the [hr-create-tables.sql](https://github.com/jonfernq/SimpleERP/blob/main/Human-Resources/hr-create-tables.sql) file.

### Payroll Sub-System

The process of "Time and attendance tracking: keeping track of when employees arrive and leave, calculating hours worked, and generating paychecks" is closely related to the payroll system, which is a sub-process of the human resources management system. The payroll system is responsible for processing employee paychecks, calculating taxes and other deductions, and maintaining records of all employee compensation and deductions.

The time and attendance tracking process provides the input for the payroll system by keeping track of the hours worked by each employee, which is then used to calculate their pay. The payroll system then uses this information to generate paychecks, calculate taxes and other deductions, and maintain records of all employee compensation and deductions. The two processes are closely integrated and work together to ensure that employees are paid accurately and on time.

### Expense Management
When the finance or accounting department processes employee expense reports in a small company, the typical business processes that are part of this include:
1.  Review and verify: Reviewing and verifying expense reports for compliance with company policies and guidelines
2.  Reimburse or pay: Processing employee reimbursements and/or payments for expenses
3.  Record and track: Recording and tracking expenses in the company's financial system or accounting software
4.  Audit and reconcile: Auditing and reconciling expenses with credit card statements or receipts
5.  Analyze and report:  Generating reports and analysis of expense data to identify trends or areas for cost savings
6.  Communicate and educate: Communicating with employees and managers regarding expense policies and procedures.

### EM BD Tables

![expense-management](https://user-images.githubusercontent.com/68504324/213843875-5ff744d3-77c4-402d-b50f-f19758ab7d90.png)

EM DB tables are described by SQL Create statements in the [em-create-tables.sql](https://github.com/jonfernq/SimpleERP/blob/main/Human-Resources/em-create-tables.sql) file.

