import os

cur_dir = os.getcwd() 
print "you are in {}".format(cur_dir)
for file in os.listdir(cur_dir):
    if file != 'rename.py':
        os.rename(file, 'new' + file)
    
