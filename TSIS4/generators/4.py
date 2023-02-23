def down(n):
    while n>=0:
        yield n
        n-=1
b=int(input())
res=[]
for i in down(b):
    res.append(str(i))

print (' '.join(res))