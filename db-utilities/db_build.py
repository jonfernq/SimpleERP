import os, re, dirwalk_regex, execute_sql 

# db_build.py - 
# walk sub-directories from root directory
# collecting all '.sql' files, executing each
# best to uncomment execute after verifying files 

def main():
    root_dir = os.getcwd() 
    os.chdir('SimpleERP')
    root_dir = os.getcwd() 
    print(os.listdir()) 
    
    regex = '^.*-create-tables\.sql$'
    files = dirwalk_regex.find_files(root_dir, regex)

'CREATE DATABASE SimpleERP;'

    for file, full_path in files:
        print(f'{file} : {full_path}')
        # execute_sql_file(full_path)

if __name__ == "__main__":
    main()
