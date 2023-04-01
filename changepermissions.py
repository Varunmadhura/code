import os
file_path = raw_input("Enter the file or directory path: ")
mode = int(raw_input("Enter the permissions in octal notation (e.g. 0o755): "), 8)
os.chmod(file_path, mode)
print("Permissions changed successfully.")
