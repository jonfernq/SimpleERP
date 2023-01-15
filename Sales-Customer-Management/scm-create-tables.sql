
/* The sales and customer management system for a small company requires relational database tables to store and manage customer information, sales data, and other related information: */ 

-- Customer table:

CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Company VARCHAR(255),
    Address VARCHAR(255),
    Phone VARCHAR(20),
    Email VARCHAR(255)
);

-- Order table:

CREATE TABLE Order (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    ShippingAddress VARCHAR(255),
    TotalCost DECIMAL(10,2),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

-- Order Item table:

CREATE TABLE OrderItem (
    OrderItemID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    Price DECIMAL(10,2),
    FOREIGN KEY (OrderID) REFERENCES Order(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

-- Invoice table:

CREATE TABLE Invoice (
    InvoiceID INT PRIMARY KEY,
    OrderID INT,
    InvoiceDate DATE,
    TotalCost DECIMAL(10,2),
    FOREIGN KEY (OrderID) REFERENCES Order(OrderID)
);

-- Product table:

CREATE TABLE Product (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50),
    Description TEXT,
    Price DECIMAL(10,2),
    Quantity INT,
);

-- Customer Service table:

CREATE TABLE CustomerService (
    ServiceID INT PRIMARY KEY,
    CustomerID INT,
    ContactDate DATE,
    ContactType VARCHAR(50),
    Description TEXT,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

