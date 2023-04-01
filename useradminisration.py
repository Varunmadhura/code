import subprocess
while True:
   print("1. Set the user information")
   print("2. Set the password for the user")
   print("3. Set the password aging:")
   print("4. Quit")
   option = raw_input("Enter the number (1-4):")
   if option == "1":
      username = raw_input("enter the username:")
      user_id = raw_input("enter the userid:")
      group = raw_input("enter the group:")
      home_directory = raw_input("enter the home directory path:")
      shell = raw_input("enter the shell:")
      comment = raw_input("enter the comment:")
      subprocess.call(['useradd', '-u', user_id , '-g', group ,'-d', home_directory, '-s', shell ,'-c', comment , username])
      print(subprocess.call)
   elif option == "2":
      username = raw_input("enter the username.")
      subprocess.call(["passwd",username])
   elif option == "3":
       username = raw_input("Enter the username:")
       min_days = raw_input("Enter the min no of days:")
       Max_days = raw_input("Enter the max no of days:")
       warn_date = raw_input("Enter the waarning date:")
       acc_inactive = raw_input("Enter when the account to be Inactive:")
       subprocess.call(['chage','-m', min_days , '-M' , Max_days , '-W' , warn_date , '-I' , acc_inactive , username])
   elif option == "4":
       print("QUIT")
       break   
   else:
     print("INVALID OPTION PLEASE TRY AGAIN.")
