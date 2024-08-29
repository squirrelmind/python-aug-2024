import os

# Initialize an empty list to store the file information
file_info_list = []

# Get the list of all files in the current working directory
files = os.listdir()

# Loop through each file in the directory
for file in files:
    # Check if the item is a file (not a directory)
    if os.path.isfile(file):
        # Get the file size
        file_size = os.path.getsize(file)
        # Create a dictionary with file name and size
        file_info = {
            'name': file,
            'size': file_size
        }
        # Add the dictionary to the list
        file_info_list.append(file_info)

# Print the list of dictionaries
print(file_info_list)
