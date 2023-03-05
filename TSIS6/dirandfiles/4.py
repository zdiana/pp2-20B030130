with open(r"abc.txt", 'r') as fp:
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)