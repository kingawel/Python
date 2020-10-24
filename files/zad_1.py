import os

dir = "." #path to the directory
files = next(os.walk(dir))[2] #count only files, without subdirectories
file_count = len(files)
print(file_count)
