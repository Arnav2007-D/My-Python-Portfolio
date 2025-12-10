from pathlib import Path
import shutil

print("Built for lazy people like me 😊, who dont want" \
      + "to make their folders neat")
print("------------------------------------------------------------")
print("\n")
print("Enter 'C:\\Users\\YourName\\Downloads' (or Desktop/Documents) below:")
print("\n")
path = Path(input("Enter Path: "))

files_in_root = sum(1 for item in path.iterdir() if item.is_file())
if files_in_root == 0:
    print("Your files are already organised!")
    input("Press Enter to exit...")
    exit()

for item in path.iterdir():
    if item.is_file():
        ext = item.suffix[1:].lower()  
        dest_dir = path / ext
        dest_dir.mkdir(exist_ok=True)
        shutil.move(str(item), dest_dir / item.name)
print("Done organizing files!")
input("Press Enter to exit...")
