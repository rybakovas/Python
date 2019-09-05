from pathlib import Path


# Absolute path
#C:\Program Files\Microsoft
# Relative path
path = Path("directory")
print(path.exists())
path = Path("emails")
print(path.mkdir())
path.rmdir()

# ===============================================

path = Path()
for file in path.glob('*.py'):
    print(file)


for file in path.glob('*.txt'):
    print(file)

