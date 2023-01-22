CREATE TABLE leads (
  lead_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  phone VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  status ENUM('new', 'contacted', 'qualified', 'unqualified') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE accounts (
  account_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  phone VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE contacts (
  contact_id INT PRIMARY KEY AUTO_INCREMENT,
  account_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  phone VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (account_id) REFERENCES accounts (account_id)
);

CREATE TABLE opportunities (
  opportunity_id INT PRIMARY KEY AUTO_INCREMENT,
  account_id INT NOT NULL,
  lead_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  amount DECIMAL(10,2) NOT NULL,
  stage ENUM('prospecting', 'qualification', 'needs analysis', 'value proposition', 'id. decision makers', 'perception analysis', 'proposal/price quote', 'negotiation/review', 'closed won', 'closed lost') NOT NULL,
  probability INT NOT NULL,
  close_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (account_id) REFERENCES accounts (account_id),
  FOREIGN KEY (lead_id) REFERENCES leads (lead_id)
);

CREATE TABLE activities (
  activity_id INT PRIMARY KEY AUTO_INCREMENT,
  opportunity_id INT NOT NULL,
  subject VARCHAR(255) NOT NULL,
  notes TEXT NOT NULL,
  date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (opportunity_id) REFERENCES opportunities (opportunity_id)
);

CREATE TABLE sales_quotas (
  quota_id INT PRIMARY KEY AUTO_INCREMENT,
  salesperson_id INT NOT NULL,
  amount DECIMAL(10,2) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE sales_performance (
  sales_id INT PRIMARY KEY AUTO_INCREMENT,
  salesperson_id INT NOT NULL,
  opportunity_id INT NOT NULL,
  amount DECIMAL(10,2) NOT NULL,
  closed_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (salesperson_id) REFERENCES salespeople (salesperson_id),
  FOREIGN KEY (opportunity_id) REFERENCES opportunities (opportunity_id)
);

CREATE TABLE salespeople (
  salesperson_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  phone VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



