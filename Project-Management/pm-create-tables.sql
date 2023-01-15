
/* A project management system for a small company require relational database tables to store and manage project information, task data, and other related information: */

-- Project table:

CREATE TABLE Project (
    ProjectID INT PRIMARY KEY,
    ProjectName VARCHAR(255),
    Description TEXT,
    StartDate DATE,
    EndDate DATE,
    Budget DECIMAL(10,2),
    Status VARCHAR(20)
);

-- Task table:

CREATE TABLE Task (
    TaskID INT PRIMARY KEY,
    ProjectID INT,
    TaskName VARCHAR(255),
    Description TEXT,
    StartDate DATE,
    EndDate DATE,
    Status VARCHAR(20),
    FOREIGN KEY (ProjectID) REFERENCES Project(ProjectID)
);

-- Resource table:

CREATE TABLE Resource (
    ResourceID INT PRIMARY KEY,
    ResourceName VARCHAR(255),
    Type VARCHAR(20),
    Cost DECIMAL(10,2)
);

-- Project Resource table:

CREATE TABLE ProjectResource (
    ProjectResourceID INT PRIMARY KEY,
    ProjectID INT,
    ResourceID INT,
    Quantity INT,
    FOREIGN KEY (ProjectID) REFERENCES Project(ProjectID),
    FOREIGN KEY (ResourceID) REFERENCES Resource(ResourceID)
);

-- Budget table:

CREATE TABLE Budget (
    BudgetID INT PRIMARY KEY,
    ProjectID INT,
    ResourceID INT,
    Cost DECIMAL(10,2),
    FOREIGN KEY (ProjectID) REFERENCES Project(ProjectID),
    FOREIGN KEY (ResourceID) REFERENCES Resource(ResourceID)
);

-- Timesheet table:

CREATE TABLE Timesheet (
    TimesheetID INT PRIMARY KEY,
    ProjectID INT,
    EmployeeID INT,
    TaskID INT,
    StartTime DATETIME,
    EndTime DATETIME,
    FOREIGN KEY (ProjectID) REFERENCES Project(ProjectID),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
    FOREIGN KEY (TaskID) REFERENCES Task(TaskID)
);

-- Milestone table:

CREATE TABLE Milestone (
    MilestoneID INT PRIMARY KEY,
    ProjectID INT,
    MilestoneName VARCHAR(255),
    Description TEXT,
    DueDate DATE,
    Status VARCHAR(20),
    FOREIGN KEY (ProjectID) REFERENCES Project(ProjectID)
);



