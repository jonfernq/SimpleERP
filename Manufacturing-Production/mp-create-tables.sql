
/* A manufacturing and production system for a small company requires relational database tables to store and manage production information, inventory data, and other related information: */ 

-- Product table:

CREATE TABLE Product (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50),
    Description TEXT,
    Price DECIMAL(10,2)
);

-- Bill of Materials (BOM) table:

CREATE TABLE BOM (
    BOMID INT PRIMARY KEY,
    ProductID INT,
    ComponentID INT,
    Quantity INT,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
    FOREIGN KEY (ComponentID) REFERENCES Product(ProductID)
);

-- Production Order table:

CREATE TABLE ProductionOrder (
    OrderID INT PRIMARY KEY,
    ProductID INT,
    Quantity INT,
    DueDate DATE,
    Status VARCHAR(20),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

-- Work Order table:

CREATE TABLE WorkOrder (
    WorkOrderID INT PRIMARY KEY,
    OrderID INT,
    StartDate DATE,
    EndDate DATE,
    FOREIGN KEY (OrderID) REFERENCES ProductionOrder(OrderID)
);

-- Inventory table:

CREATE TABLE Inventory (
    InventoryID INT PRIMARY KEY,
    ProductID INT,
    Quantity INT,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

-- Machine table:

CREATE TABLE Machine (
    MachineID INT PRIMARY KEY,
    MachineName VARCHAR(50),
    Description TEXT,
    Type VARCHAR(50)
);

-- Production schedule table:

CREATE TABLE ProductionSchedule (
    ScheduleID INT PRIMARY KEY,
    WorkOrderID INT,
    MachineID INT,
    StartTime DATETIME,
    EndTime DATETIME,
    FOREIGN KEY (WorkOrderID) REFERENCES WorkOrder(WorkOrderID),
    FOREIGN KEY (MachineID) REFERENCES Machine(MachineID)
);


