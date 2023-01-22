from faker import Faker
import random

# Connect to the database
# ...
# Connect to the database
import mysql.connector

mydb = mysql.connector.connect(
  host="hostname",
  user="username",
  password="password",
  database="databasename"
)

mycursor = mydb.cursor()

# Create a Faker instance
fake = Faker()

# Create a list of fake leads
leads = []
for _ in range(100):
    leads.append({
        'name': fake.name(),
        'email': fake.email(),
        'phone': fake.phone_number(),
        'address': fake.address(),
        'status': random.choice(['new', 'contacted', 'qualified', 'unqualified'])
    })

# Insert the leads into the database
# ...
# Insert the leads into the database
for lead in leads:
    sql = "INSERT INTO leads (name, email, phone, address, status) VALUES (%s, %s, %s, %s, %s)"
    val = (lead['name'], lead['email'], lead['phone'], lead['address'], lead['status'])
    mycursor.execute(sql, val)
mydb.commit()

# Create a list of fake accounts
accounts = []
for _ in range(50):
    accounts.append({
        'name': fake.company(),
        'email': fake.company_email(),
        'phone': fake.phone_number(),
        'address': fake.address()
    })

# Insert the accounts into the database
# ...
# Insert the accounts into the database
for account in accounts:
    sql = "INSERT INTO accounts (name, email, phone, address) VALUES (%s, %s, %s, %s)"
    val = (account['name'], account['email'], account['phone'], account['address'])
    mycursor.execute(sql, val)
mydb.commit()

# Create a list of fake contacts
contacts = []
for account in accounts:
    for _ in range(random.randint(1, 5)):
        contacts.append({
            'account_id': account['account_id'],
            'name': fake.name(),
            'email': fake.email(),
            'phone': fake.phone_number()
        })

# Insert the contacts into the database
# ...
# Insert the contacts into the database
for contact in contacts:
    sql = "INSERT INTO contacts (account_id, name, email, phone) VALUES (%s, %s, %s, %s)"
    val = (contact['account_id'], contact['name'], contact['email'], contact['phone'])
    mycursor.execute(sql, val)
mydb.commit()

# Create a list of fake opportunities
opportunities = []
for lead in leads:
    for account in accounts:
        if random.random() < 0.1:
            opportunities.append({
                'lead_id': lead['lead_id'],
                'account_id': account['account_id'],
                'name': fake.bs(),
                'amount': fake.random_int(min=1000, max=100000, step=1000),
                'stage': random.choice(['prospecting', 'qualification', 'needs analysis', 'value proposition', 'id. decision makers', 'perception analysis', 'proposal/price quote', 'negotiation/review', 'closed won', 'closed lost']),
                'probability': random.randint(1, 100),
                'close_date': fake.date_between(start_date='+1y', end_date='+2y')
            })

# Insert the opportunities into the database
# ...
# Insert the opportunities into the database
for opportunity in opportunities:
    sql = "INSERT INTO opportunities (lead_id, account_id, name, amount, stage, probability, close_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (opportunity['lead_id'], opportunity['account_id'], opportunity['name'], opportunity['amount'], opportunity['stage'], opportunity['probability'], opportunity['close_date'])
    mycursor.execute(sql, val)
mydb.commit()


# Create a list of fake activities
activities = []
for opportunity in opportunities:
    for _ in range(random.randint(1, 5)):
        activities.append({
            'opportunity_id': opportunity['opportunity_id'],
            'subject': fake.sentence(nb_words=6, variable_nb_words=True),
            'notes': fake.paragraph(),
            'date': fake.date_between(start_date='-1y', end_date='+1y')
        })

# Insert the activities into the database
# ...

# Insert the activities into the database
for activity in activities:
    sql = "INSERT INTO activities (opportunity_id, subject, notes, date) VALUES (%s, %s, %s, %s)"
    val = (activity['opportunity_id'], activity['subject'], activity['notes'], activity['date'])
    mycursor.execute(sql, val)
mydb.commit()

# Create a list of fake sales quotas
sales_quotas = []
for i in range(10):
    sales_quotas.append({
        'salesperson_id': i+1,
        'amount': fake.random_int(min=1000, max=100000, step=1000),
        'start_date': fake.date_between(start_date='-1y', end_date='-1m'),
        'end_date': fake.date_between(start_date='-1m', end_date='+1y')
    })

# Insert the sales quotas into the database
# ...

# Insert the sales quotas into the database
for quota in sales_quotas:
    sql = "INSERT INTO sales_quotas (salesperson_id, amount, start_date, end_date) VALUES (%s, %s, %s, %s)"
    val = (quota['salesperson_id'], quota['amount'], quota['start_date'], quota['end_date'])
    mycursor.execute(sql, val)
mydb.commit()


# Create a list of fake sales performance
sales_performance = []
for i in range(len(opportunities)):
    sales_performance.append({
        'salesperson_id': i%10 +1,
        'opportunity_id': i+1,
        'amount': opportunities[i]['amount'],
        'closed_date': opportunities[i]['close_date']
    })

# Insert the sales performance into the database
# ...

# Insert the sales performance into the database
for performance in sales_performance:
    sql = "INSERT INTO sales_performance (salesperson_id, opportunity_id, amount, closed_date) VALUES (%s, %s, %s, %s)"
    val = (performance['salesperson_id'], performance['opportunity_id'], performance['amount'], performance['closed_date'])
    mycursor.execute(sql, val)
mydb.commit()

# Create a list of fake salespeople
salespeople = []
for i in range(10):
    salespeople.append({
        'name': fake.name(),
        'email': fake.email(),
        'phone': fake.phone_number()
    })

# Insert the salespeople into the database
# ...


# Insert the salespeople into the database
for salesperson in salespeople:
    sql = "INSERT INTO salespeople (name, email, phone) VALUES (%s, %s, %s)"
    val = (salesperson['name'], salesperson['email'], salesperson['phone'])
    mycursor.execute(sql, val)
mydb.commit()

# Close the cursor and the database connection
mycursor.close()
mydb.close()
