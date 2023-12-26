from math import gcd
t=int(input())
st=[]
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    d=0
    for j in a :
       if j % k == 0 :
           d = gcd(d,j//k)
    if d==1 :
        print("YES")
    else:
        print("NO")  