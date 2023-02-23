def even(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1
a=int(input())
l=[]
for i in even(a):
    l.append(str(i))

print (','.join(l))