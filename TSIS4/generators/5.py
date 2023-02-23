def squares(a,b):
    while a<=b:
        yield a**2
        a+=1
x=int(input())
y=int(input())
for i in squares(x,y):
    print(i)