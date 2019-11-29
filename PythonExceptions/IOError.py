
try:
    #this will throw an exception if the file doesn't exist.
    fs = open("file.txt","r")
except IOError:
    print("File not found")
else:
    print("The file opened successfully")
    fs.close()
