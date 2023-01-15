/* The relational database tables with SQL Create code that are needed for a 'payroll system' for a small company.
A payroll system for a small company would likely require several relational database tables in order to store and manage employee information, payroll data, and other related information. Here is an example of SQL code that could be used to create some of the tables that might be needed: */ 

-- Employee table:

CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Address VARCHAR(255),
    Phone VARCHAR(20),
    Email VARCHAR(255),
    SocialSecurityNumber VARCHAR(11),
    HireDate DATE,
    Salary DECIMAL(10,2),
    TaxRate DECIMAL(5,2)
);

-- Payroll table:

CREATE TABLE Payroll (
    PayrollID INT PRIMARY KEY,
    EmployeeID INT,
    PayPeriodStart DATE,
    PayPeriodEnd DATE,
    HoursWorked DECIMAL(5,2),
    GrossPay DECIMAL(10,2),
    Deductions DECIMAL(10,2),
    NetPay DECIMAL(10,2),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

-- Deduction table:

CREATE TABLE Deduction (
    DeductionID INT PRIMARY KEY,
    EmployeeID INT,
    DeductionType VARCHAR(50),
    Amount DECIMAL(10,2),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

-- Timeclock table:

CREATE TABLE Timeclock (
    TimeclockID INT PRIMARY KEY,
    EmployeeID INT,
    ClockIn DATETIME,
    ClockOut DATETIME,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);


