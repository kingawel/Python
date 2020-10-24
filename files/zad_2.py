import os
 
source = "."
 
def print_files(dir):
 
   for element in os.listdir(dir):
 
       file = os.path.join(dir, element); #print path to all files in directories and subdirectories, separating by "\"
       print (file)
       if os.path.isdir(file):
           print_files(file)
 
print_files(source)