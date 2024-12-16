import os
import shutil

def organize_files(directory):
    # Ensure the directory path ends with a slash
    directory = directory.rstrip('/') + '/'

    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        if os.path.isfile(directory + filename):
            # Get the file extension
            file_ext = filename.split('.')[-1]

            # Create a subdirectory if not exists
            if not os.path.exists(directory + file_ext):
                os.makedirs(directory + file_ext)

            # Move the file to the subdirectory
            shutil.move(directory + filename, directory + file_ext + '/' + filename)

    print("File organization completed.")

# Replace with the directory path you want to organize
directory_to_organize = 'C:/Users/sumit/OneDrive/Desktop/Files_to_Organize/'

# Call the function to organize files
organize_files(directory_to_organize)
