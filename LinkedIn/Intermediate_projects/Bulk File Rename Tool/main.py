import os

folder_path = input("Enter full folder path: ")
extension = input("Enter file extension that you want to rename (e.g. .png) :")
prefix = input("Enter prefix (e.g holiday) :")

# get a list of all files in the folder
all_files = os.listdir(folder_path)

# filter the list to only include files with the given extension
files_with_extension = [file for file in all_files if file.endswith(extension)]

print(files_with_extension)
