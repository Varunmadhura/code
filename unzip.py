import subprocess
zipped_filepath = raw_input("enter the zipped file path :")
subprocess.call(['gunzip',zipped_filepath])
print("The file is successfully uncompressed")
