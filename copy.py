import shutil
source=raw_input("enter the source file:")
destination=raw_input("enter the destination file:")
shutil.copyfile(source,destination)
print(destination,"is copied")
