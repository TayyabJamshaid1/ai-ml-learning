import os

# Specify the directory path
# Use '.' for the current directory where the script is running
# Or provide a full path like: directory_path = '/path/to/your/folder'
directory_path = '.'

# Get the list of all files and directories
try:
    contents = os.listdir(directory_path)
    
    # Print the contents
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)
        
except FileNotFoundError:
    print(f"Error: The directory '{directory_path}' was not found.")
except PermissionError:
    print(f"Error: Permission denied to access '{directory_path}'.")