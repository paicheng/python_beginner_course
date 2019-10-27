import os

os.system("cls")
current_path = os.path.abspath(__file__)
print(current_path)
current_dir = os.path.dirname(__file__)
print(current_dir)

tree = os.walk(current_dir)
for current_path, sub_dir, files in tree:
    print('current path:', current_path)
    print('sub dir:', sub_dir)
    print('files in current:', files)
    print("="*50)

tree = os.walk(current_dir)
for r in tree:
    print(r)
