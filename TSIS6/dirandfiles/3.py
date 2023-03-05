import os
print("Test a path exists or not:")
path = r'C:\CPP\PP2\TSIS6\dirandfiles\a.txt'
print(os.path.exists(path))
path = r'C:\CPP\PP2\TSIS6\dirandfiles\a.txt'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))