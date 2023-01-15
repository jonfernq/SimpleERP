
/* The relational database tables with SQL Create code that are needed for a 'general ledger' for a small company. */ 

/* A general ledger is a record of a company's financial transactions and is typically organized into several 
different categories such as accounts payable, accounts receivable, cash, and general ledger. To implement a 
general ledger for a small company using a relational database, you would need to create several tables to store 
the different types of data.

Here is an example of the SQL CREATE code for the tables that would be needed for a general ledger for a small company:  */ 

-- Accounts table:

CREATE TABLE Accounts (
    AccountID INT PRIMARY KEY,
    AccountName VARCHAR(255) NOT NULL,
    AccountType VARCHAR(255) NOT NULL
);

/* This table will hold the different types of accounts in the general ledger, such as accounts payable, 
accounts receivable, and cash. The AccountID is the primary key and AccountName and AccountType are the 
columns that store the name and type of the account respectively. */ 

-- Journal table:

CREATE TABLE Journal (
    JournalID INT PRIMARY KEY,
    JournalDate DATE NOT NULL,
    JournalDescription VARCHAR(255) NOT NULL
);

/* This table will hold the journal entries for the general ledger. The JournalID is the primary key, 
JournalDate is the date of the journal entry, and JournalDescription is a brief description of the journal entry. */ 

-- JournalEntries table:

CREATE TABLE JournalEntries (
    JournalEntryID INT PRIMARY KEY,
    JournalID INT NOT NULL,
    AccountID INT NOT NULL,
    Debit DECIMAL(10,2) NOT NULL,
    Credit DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (JournalID) REFERENCES Journal(JournalID),
    FOREIGN KEY (AccountID) REFERENCES Accounts(AccountID)
);

/* This table will hold the individual entries for each journal entry. The JournalEntryID is the primary key, 
JournalID is a foreign key referencing the Journal table, AccountID is a foreign key referencing the Accounts 

table, Debit is the amount debited to the account and Credit is the amount credited to the account. */ 

/* The above tables are the basic structure of a general ledger, it can be enhanced with more columns 
to meet more specific needs, you can also add more tables to track more information such as customers, 
vendors, and inventory. */ 
