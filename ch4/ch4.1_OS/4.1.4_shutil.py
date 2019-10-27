import shutil
import os

os.system('cls')
# shutil.copy
if os.path.exists('yourfile.txt'):
    oldpath = os.path.abspath('yourfile.txt')
    olddir, oldfilename = os.path.split(oldpath)
    newdir = os.path.join(olddir, 'dir3')
    if not os.path.exists(newdir):
        os.mkdir(newdir)
    shutil.copy(oldpath, os.path.join(newdir, 'yourfile.txt'))

# shutil.copytree
olddir = os.path.abspath('dir2')
newdir = os.path.abspath('dir4')
if os.path.exists(olddir):
    shutil.copytree(olddir, newdir)

# shutil.rmtree
shutil.rmtree(newdir)

# shutil.move
shutil.move(olddir, newdir)
