import os
print('Exist:', os.access('C:\CPP\PP2', os.F_OK))
print('Readable:', os.access('C:\CPP\PP2', os.R_OK))
print('Writable:', os.access('C:\CPP\PP2', os.W_OK))
print('Executable:', os.access('C:\CPP\PP2', os.X_OK))