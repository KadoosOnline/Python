import os

# Does a file exist?
print(os.path.exists('a.txt'))

# Delete a file - but only after checking, otherwise FileNotFoundError.
if os.path.exists('to_delete.txt'):
    os.remove('to_delete.txt')
else:
    print('to_delete.txt does not exist')

# Where am I?
print('current folder:', os.getcwd())

# What is in this folder?
print(os.listdir('.'))

# Building a path that works on Windows, Linux and macOS.
path = os.path.join('data', 'students', 'list.txt')
print(path)

# Splitting a path.
print(os.path.basename(path))     # list.txt
print(os.path.dirname(path))      # data/students
print(os.path.splitext('app.py')) # ('app', '.py')

# Creating and removing folders.
os.makedirs('demo_folder', exist_ok=True)   # exist_ok avoids an error
print(os.path.isdir('demo_folder'))
os.rmdir('demo_folder')                     # only works on an EMPTY folder

# Size of a file, in bytes.
print(os.path.getsize('a.txt'))
