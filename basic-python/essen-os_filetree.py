import os

for root, dirs, files in os.walk('.'):
    print("In folder:", root)
    print("Subfolders:", dirs)
    print("Files:", files)


file_path = os.path.join('folder', 'subfolder', 'file.txt')

# create
with open('file.txt', 'w') as f:
    f.write("Hello!")

# delete
os.remove('file.txt')

files = os.listdir('.')
print(files)

cwd = os.getcwd()
print("Current dir:", cwd)

# os.chdir('/path/to/your/folder')