import shutil
source=raw_input('enter the source path:')
destination=raw_input('enter the destination path:')
shutil.move(source,destination)
print("moved successfully")
