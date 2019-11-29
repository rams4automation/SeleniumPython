import os

if os.path.exists("C://Users//E004373//Desktop//Python//demofile1.txt"):
    os.remove("C://Users//E004373//Desktop//Python//demofile1.txt")
    print("The file deleted successfully")
else:
    print("The file does not exist")


# Delete Folder

os.rmdir("C://Users//E004373//Desktop//Python1")

