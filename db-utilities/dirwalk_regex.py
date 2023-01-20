import os
import re

# dirwalk_regex.py - 
# walk directory structure, from root directory 
# to all dub-directories, collecting filename and 
# full path, then print out 

def find_files(root_dir, regex):
    matches = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if re.search(regex, file):
                full_path = os.path.join(root, file)
                matches.append((file, full_path))
    return matches

def main():
    # root_dir = '/path/to/root/directory'
    root_dir = os.getcwd() 
    # regex = '^.*\.txt$'
    regex = '^.*\.sql$' 
    files = find_files(root_dir, regex)
    for file, full_path in files:
        print(f'{file} : {full_path}')

if __name__ == "__main__":
    main()

