n=int(input(""))
flag = 0
for i in range(2,n+1,2):
    if(n%i==0):
        print(i,end=" ")
        flag = 1
        
        
if(flag==0):
    print("-1")