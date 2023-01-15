
/* A 'distribution and logistics' system for managing the distribution and logistics of goods and services, including warehouse management and transportation, requires relational database tables: */ 

-- Warehouse table:

CREATE TABLE Warehouse (
    WarehouseID INT PRIMARY KEY,
    WarehouseName VARCHAR(255),
    Address VARCHAR(255),
    Phone VARCHAR(20),
    Email VARCHAR(255)
);

-- Product table:

CREATE TABLE Product (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(255),
    Description TEXT,
    Price DECIMAL(10,2)
);

-- Stock table:

CREATE TABLE Stock (
    StockID INT PRIMARY KEY,
    WarehouseID INT,
    ProductID INT,
    Quantity INT,
    FOREIGN KEY (WarehouseID) REFERENCES Warehouse(WarehouseID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

-- PurchaseOrder table:

CREATE TABLE PurchaseOrder (
    OrderID INT PRIMARY KEY,
    SupplierID INT,
    OrderDate DATE,
    TotalAmount DECIMAL(10,2),
    Status VARCHAR(20),
    FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID)
);

-- PurchaseOrderLine table:

CREATE TABLE PurchaseOrderLine (
    OrderLineID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    Price DECIMAL(10,2),
    FOREIGN KEY (OrderID) REFERENCES PurchaseOrder(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

-- Shipment table:

CREATE TABLE Shipment (
    ShipmentID INT PRIMARY KEY,
    OrderID INT,
    ShipmentDate DATE,
    Carrier VARCHAR(255),
    TrackingNumber VARCHAR(255),
    FOREIGN KEY (OrderID) REFERENCES PurchaseOrder(OrderID)
);

-- Delivery table:

CREATE TABLE Delivery (
    DeliveryID INT PRIMARY KEY,
    ShipmentID INT,
    WarehouseID INT,
    DeliveryDate DATE,
    FOREIGN KEY (ShipmentID) REFERENCES Shipment(ShipmentID),
    FOREIGN KEY (WarehouseID) REFERENCES Warehouse(WarehouseID)
);

-- Invoice table:

CREATE TABLE Invoice (
    InvoiceID INT PRIMARY KEY,
    OrderID INT,
    InvoiceDate DATE,
    TotalAmount DECIMAL(10,2),
    FOREIGN KEY (OrderID) REFERENCES PurchaseOrder(OrderID)
);

-- Payment table:

CREATE TABLE Payment (
    PaymentID INT PRIMARY KEY,
    InvoiceID INT,
    PaymentDate DATE,
    Amount DECIMAL(10,2),
    PaymentMethod VARCHAR(20),
    FOREIGN KEY (InvoiceID) REFERENCES Invoice(InvoiceID)
);

-- Transportation table:

CREATE TABLE Transportation (
    TransportationID INT PRIMARY KEY,
    ShipmentID INT,
    Carrier VARCHAR(255),
    TrackingNumber VARCHAR(255),
    DepartureDate DATE,
    ArrivalDate DATE,
    FOREIGN KEY (ShipmentID) REFERENCES Shipment(ShipmentID)
);

-- Vehicle table:

CREATE TABLE Vehicle (
    VehicleID INT PRIMARY KEY,
    LicensePlate VARCHAR(20),
    Type VARCHAR(50),
    Make VARCHAR(50),
    Model VARCHAR(50),
    Year INT
);

-- Route table:

CREATE TABLE Route (
    RouteID INT PRIMARY KEY,
    TransportationID INT,
    VehicleID INT,
    Driver VARCHAR(255),
    StartLocation VARCHAR(255),
    EndLocation VARCHAR(255),
    FOREIGN KEY (TransportationID) REFERENCES Transportation(TransportationID),
    FOREIGN KEY (VehicleID) REFERENCES Vehicle(VehicleID)
);







