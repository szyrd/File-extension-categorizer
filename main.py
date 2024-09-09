import os
from collections import defaultdict

def categorize_files_by_type(folder_path):
    
    files_by_type = defaultdict(list)
    
    # Check if the folder exists and is a directory
    if not os.path.isdir(folder_path):
        raise ValueError(f"The path {folder_path} does not exist or is not a directory.")
    
    # Walk through the directory structure
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_ext = os.path.splitext(file)[1]  # Get file extension
            files_by_type[file_ext].append(file_path)
    
    return dict(files_by_type)

# Print the categorized files
def print_categorized_files(files_dict):
    for file_type, files in files_dict.items():
        print(f"File Type: {file_type}")
        for file in files:
            print(f"    {file}")

if __name__ == "__main__":
    # Ask the user to input the folder path
    folder_path = input("Please enter the folder path: ")
    
    try:
        result = categorize_files_by_type(folder_path)
        print_categorized_files(result)
    except ValueError as e:
        print(e)
