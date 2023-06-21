import os

folder_path = input("Enter full folder path: ")
extension = input("Enter file extension that you want to rename (e.g. .png) :")
prefix = input("Enter prefix (e.g holiday) :")

# get a list of all files in the folder
all_files = os.listdir(folder_path)
print(all_files)
