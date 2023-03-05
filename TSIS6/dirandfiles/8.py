import os
 
file = 'file1.txt'
 

location = "C:\CPP\PP2\TSIS5"
 

path = os.path.join(location, file)
 

os.remove(path)