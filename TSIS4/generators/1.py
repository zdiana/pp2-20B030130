def sqr(n):
    i=0
    while i<=n:
        yield i**2
        i+=1
a=int(input())
res=sqr(a)
print (next(res))
print (next(res))
print (next(res))