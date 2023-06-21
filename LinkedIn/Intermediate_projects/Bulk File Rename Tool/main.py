import os

folder_path = input("Enter full folder path: ")
extension = input("Enter file extension that you want to rename (e.g. .png) :")
prefix = input("Enter prefix (e.g holiday) :")

# get a list of all files in the folder
all_files = os.listdir(folder_path)

# filter the list to only include files with the given extension
files_with_extension = [file for file in all_files if file.endswith(extension)]

# loop through the files and rename them with the given prefix
for i, file in enumerate(files_with_extension):
    new_name = f"{prefix}{i+1}{extension}"
    print(f"Renaming {file} to {new_name}")
    os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))

print(f"All done! Renamed {len(files_with_extension)} files.")
