def div(n):
    i=0
    while i<=n:
        if i%3==0 and i%4==0:
            yield i
        i+=1
a=int(input())
l=[]
for i in div(a):
    l.append(str(i))

print (' '.join(l))