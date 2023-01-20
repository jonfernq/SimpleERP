import sqlite3

# execute_sql.py - 
# execute an '.sql' file 

def execute_sql_file(file_path):
    # Connect to an SQLite database
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Read the SQL file
    with open(file_path, 'r') as file:
        sql = file.read()

    # Split the SQL file into individual statements
    statements = sql.split(';')

    # Execute each statement
    for statement in statements:
        cursor.execute(statement)

    # Commit the changes to the database
    conn.commit()

    # Close the connection
    cursor.close()
    conn.close()

def main():
    # Example usage
    execute_sql_file("example.sql")

if __name__ == "__main__":
    main()
