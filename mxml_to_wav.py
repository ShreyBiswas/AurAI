import os

files = os.listdir()
print(files)
files = [os.path.join(os.chdir(),file) for file in files]
print(files)