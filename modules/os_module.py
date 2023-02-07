f = open('practice.txt','w+')
f.write('This is a test')
f.close

import os 
print(os.getcwd()) # returns current working directory
# takes a path as an arguement and lists everything there. ex: C:\Users
print(os.listdir()) # lists everything in current working directory

import shutil
# takes source and destination as args, takes file and moves to destination
shutil.move('practice.txt', 'C:\Users\thega\Desktop')
file_path = 'c/Users/thega/Desktop/LearningPython/modules/os_module.py'
#dirpath, dirnames, filenames
for folder, sub_folders, files in os.walk(file_path):
  print(f"Currently looking at {folder}")
  print('\n')
  print("The subfolders are: ")
  for sub_fold in sub_folders:
    print(f'\tSubfolder: {sub_fold}')
    print('\n')
  for f in files:
    print(f'\tFile: {f}')
    print('\n')