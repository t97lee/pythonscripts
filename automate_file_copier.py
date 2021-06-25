'''
Automated File Copier (based off file type)

Uses glob.iglob() within a for loop to iterate through the parent and child directories to find any file type that matches .jpg (or any other file type)
which then copies to a new directory.

src_dir: source directory (as a raw string to prevent the \U unicode error)
dst_dir: destination directory 
'''

import glob
from shutil import copy, SameFileError
import time 

start_time = time.time()

src_dir = r"your\source\directory"
dst_dir = r"your\destination\directory"

#error handling to pass over the SameFileError
try:
    for file in glob.iglob(f"{src_dir}/**/*.jpg", recursive=True):
        copy(file, dst_dir)
except SameFileError: 
    pass

#Prints the time of the script
total_time = time.time() - start_time
print(f"{total_time} seconds")