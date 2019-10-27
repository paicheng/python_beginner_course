import os
import os.path as p

os.system("cls")

path = p.abspath(__file__)
print('abspath:', path)

basename = p.basename(__file__)
print('basename:', basename)

dirname = p.dirname(__file__)
print('dirname:', dirname)

print('exists:', p.exists(__file__))
print('getsize:', p.getsize(__file__))
print('isabs:', p.isabs(__file__))
print('isfile:', p.isfile(__file__))
print('isdir:', p.isdir(__file__))
print('split:', p.split(__file__))
print('splitdrive:', p.splitdrive(__file__))

newpath = p.join(dirname, 'temp', basename)
print('is newpath a abspath?', p.isabs(newpath))
print('join:', newpath)
# print(__file__)
