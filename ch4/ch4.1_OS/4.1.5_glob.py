import glob
import os

os.system('cls')
files = glob.glob('*.txt')+glob.glob('*os*')+glob.glob('dir*')
for file in files:
    print(file)
    print('is a directory?', os.path.isdir(file))
    print('='*50)
