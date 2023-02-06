## Database Utilities

Python code to create, populate with synthetic artificial test data, and produce reports from, the SQLite databases of the SimpleERP system.

### Database Creation

- [execute_sql.py](https://github.com/jonfernq/SimpleERP/blob/main/db-utilities/execute-sql.py): execute a '.sql' file.
- [dirwalk_regex.py](https://github.com/jonfernq/SimpleERP/blob/main/db-utilities/dirwalk_regex.py): walk directory structure, from the root directory to all sub-directories, collecting filename and  full path, then print out  
- [db_build.py](https://github.com/jonfernq/SimpleERP/blob/main/db-utilities/db_build.py): walk sub-directories from root directory collecting all '.sql' files, executing each best to uncomment execute after verifying files 
- [accumulate_sql_files.py](https://github.com/jonfernq/SimpleERP/blob/main/db-utilities/accumulate_sql_files.py): accumulate all '.sql' files into one file and execute 
- [generate_testdates_between.py](https://github.com/jonfernq/SimpleERP/blob/main/db-utilities/generate_testdates_between.py): with Faker generates n random test dates within a date range
- [generate_test_orders.py](https://github.com/jonfernq/SimpleERP/blob/main/db-utilities/generate_test_orders.py): generates n test orders with a few order items consisting of a random product id, quantity, and price, at random dates between two given dates.   
