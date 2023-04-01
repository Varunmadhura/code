import subprocess
username = raw_input("Enter the username:")
subprocess.call(["useradd",username])
subprocess.call(["passwd",username])
print("username and password added successfully")
