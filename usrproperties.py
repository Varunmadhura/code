import subprocess
username = raw_input("enter the username:")
user_id = raw_input("enter the userid:")
group = raw_input("enter the group:")
home_directory = raw_input("enter the home directory path:")
shell = raw_input("enter the shell:")
comment = raw_input("enter the comment:")
subprocess.call(['useradd', '-u', user_id , '-g', group ,'-d', home_directory, '-s', shell ,'-c', comment , username])
