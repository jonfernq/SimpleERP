import os
import re

# accumulate_sql_files.py - 
# accumulate all '.sql' files into 
# one file and execute 

def search_files(root_dir, regex):
    matches = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if re.search(regex, filename):
                file_path = os.path.join(dirpath, filename)
                matches.append((filename, file_path))
    return matches

def write_to_file(matches, out_file):
    with open(out_file, 'w') as f:
        for filename, file_path in matches:
            with open(file_path, 'r') as file:
                f.write(file.read())
                f.write('\n')


def main():
    root_dir = os.getcwd() 
    os.chdir('SimpleERP')
    root_dir = os.getcwd() 
    print(os.listdir())  
    regex = '^.*-create-tables\.sql$'
    
    matches = search_files(root_dir, regex)

    for filename, file_path in matches:
        print(filename, file_path)

    write_to_file(matches, 'all-create-tables.sql')
    print(os.listdir())  
    # os.system('cmd /c "sqlite3 SimpleERP.db < all-create-tables.sql"')
    os.system("D:\\ERP\\sqlite\\sqlite-tools\\sqlite3 SimpleERP.db < all-create-tables.sql")

if __name__ == "__main__":
    main()
