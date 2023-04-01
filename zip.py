import subprocess
file_path=raw_input("Enter the file path :")
subprocess.call(['gzip',file_path])
print("file is compressed successfully")



