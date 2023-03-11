a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)

if(0<=a,b,c<=100)
if (a==b and c==0):
    print("?")
elif (b>a+c):
    print("-")
elif (a>b+c):
    print("+")
else:
    print("0")Given a number N, print the even factors of N.If the even factor does not exists for N print '-1'.

