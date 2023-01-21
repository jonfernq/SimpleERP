-- Here is an example of the relational database tables and SQL Create code that are needed 
-- for a 'Supply Chain Management' system for a small company.
-- In this example, the "Products" table stores information about the products that the -- company sells, including the product ID, name, description, unit of measure, and price.
-- The "Vendors" table stores information about the vendors that the company buys -- products from, including the vendor ID, name, address, phone number, and email.
-- The "PurchaseOrders" table stores information about purchase orders, including the -- purchase order ID, date, and vendor ID.
-- The "PODetails" table stores the details of purchase orders, including purchase order -- detail ID, purchase order ID, product ID, quantity, and price.
-- The "Inventory" table stores the current inventory levels for each product, including -- the product ID and quantity.
 
-- Products table
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(255) NOT NULL,
    ProductDescription VARCHAR(255) NOT NULL,
    ProductUnit VARCHAR(255) NOT NULL,
    ProductPrice DECIMAL(10,2) NOT NULL
);
-- 
-- Vendors table
CREATE TABLE Vendors (
    VendorID INT PRIMARY KEY,
    VendorName VARCHAR(255) NOT NULL,
    VendorAddress VARCHAR(255) NOT NULL,
    VendorPhone VARCHAR(255) NOT NULL,
    VendorEmail VARCHAR(255) NOT NULL
);

-- Purchase Orders table
CREATE TABLE PurchaseOrders (
    POID INT PRIMARY KEY,
    PODate DATE NOT NULL,
    VendorID INT NOT NULL,
    FOREIGN KEY (VendorID) REFERENCES Vendors(VendorID)
);

-- Purchase Order Details table
CREATE TABLE PODetails (
    PODetailID INT PRIMARY KEY,
    POID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL,
    Price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (POID) REFERENCES PurchaseOrders(POID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Inventory table
CREATE TABLE Inventory (
    ProductID INT PRIMARY KEY,
    Quantity INT NOT NULL,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
