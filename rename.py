import os
import sys

print "(Linux Only)\n"
print '''This tool is used to bach rename your files. Please enter correct option:
1. Get current working directory
2. Change directory
3. Rename single file
4. Rename Multiple files
5. Exit Anytime
'''


while 1:
    choice = int(raw_input("Enter your choice: "))
    cur_dir = os.getcwd() 
    
    if choice == 1: # Print current working directory
        print "You are in: {}".format(cur_dir)
    elif choice == 2: # Change to diffrent directory
        new_path = raw_input("Enter the path (either absolute or relative): ")
        if new_path[0] == "/":
            print "you entered a absolute path. Changing to {} ...".format(new_path)
        else:
            new_path = os.path.join(cur_dir, new_path)
            print "you entered a relative path. Changing to {} ...".format(new_path)
        try:
            os.chdir(new_path)
        except OSError:
            raise
            print "Wrong Path! Try Again."
    elif choice == 3:
        old_name = raw_input("Please enter the file of directory name: ")
        new_name = raw_input("Please enter the new name: ")
        try:
            os.rename(old_name, new_name)
        except OSError:
            raise
            print "File does not exist, try again."            
    elif choice == 4:
        pass
    elif choice == 5:
        break
    else:
        print "Wrong Choice !!!"
