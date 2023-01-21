
/* SQL statements to create the tables for an employee 'expense management system': */ 

CREATE TABLE Employee (
   EmployeeID INT PRIMARY KEY,
   FirstName VARCHAR(50) NOT NULL,
   LastName VARCHAR(50) NOT NULL,
   Email VARCHAR(50) NOT NULL
);

CREATE TABLE Expense (
   ExpenseID INT PRIMARY KEY,
   EmployeeID INT NOT NULL,
   Date DATE NOT NULL,
   Description VARCHAR(255) NOT NULL,
   Amount DECIMAL(10, 2) NOT NULL,
   FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

CREATE TABLE Category (
   CategoryID INT PRIMARY KEY,
   Description VARCHAR(50) NOT NULL
);

CREATE TABLE ExpenseCategory (
   ExpenseID INT NOT NULL,
   CategoryID INT NOT NULL,
   PRIMARY KEY (ExpenseID, CategoryID),
   FOREIGN KEY (ExpenseID) REFERENCES Expense(ExpenseID),
   FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID)
);

CREATE TABLE Receipt (
   ReceiptID INT PRIMARY KEY,
   ExpenseID INT NOT NULL,
   Image BLOB NOT NULL,
   FOREIGN KEY (ExpenseID) REFERENCES Expense(ExpenseID)
);

/*  The above SQL statements create 4 tables: Employee, Expense, Category, ExpenseCategory and Receipt. 
The Employee table contains information about the employees in the company. 
The Expense table contains information about each expense, including 
the employee who incurred the expense, the date of the expense, and the amount. 
The Category table contains information about different expense categories, 
and the ExpenseCategory table creates a many-to-many relationship 
between Expense and Category. The Receipt table contains information 
about the receipts, including the expense ID and the image of the receipt.  */ 
