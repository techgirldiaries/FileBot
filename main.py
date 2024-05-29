import os

file_path = "/users/{PC Name}/{Folder Name}/{File Name}}"

print(file_path)

if os.path.isfile(file_path):
    os.remove(file_path)
    print("This file has been deleted successfully")
else:
    print("This file does NOT exist!")
