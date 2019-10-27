import os

# remove()
file = "myfile.txt"
print(os.path.abspath(file))

if os.path.exists(file):
    os.remove(file)
else:
    print(file + ' do not exist.')

# os.mkdir()
dir = 'myDir'
if not os.path.exists(dir):
    os.mkdir(dir)
else:
    print(dir + ' is there')

# os.rmdir()
dir = 'mydir'
if os.path.exists(dir):
    os.rmdir(dir)
else:
    print(dir + ' is not there')

# os.system()
current_path = os.path.dirname(__file__)
os.system('cls')
os.system('mkdir dir2')
os.system(r'copy yourFile.txt dir2\copy.txt')
os.system('notepad yourfile.txt')
