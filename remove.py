import os
import shutil

path = raw_input("Enter the file or directory path: ")

if os.path.isfile(path):
    os.remove(path)
    print("File removed successfully.")
elif os.path.isdir(path):
    shutil.rmtree(path)
    print("Directory removed successfully.")
else:
    print("Path does not exist.")
