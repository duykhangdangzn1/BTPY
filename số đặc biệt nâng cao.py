from math import *
a=int(input())
st=[]
s1=[]
for j in range(a):
    k=int(input())
    st.append(k)
k=abs(st[0]-st[1])

for i in range(1,a-1):
    k=gcd(abs(st[i]-st[i+1]),k)
s1.append(k)
for i in range(2,int(sqrt(k))+1):
     if k % i == 0:
         s1.append(i)
         if i**2 != k :
             ss=k//i
             s1.append(ss)
s1.sort()
for u in s1:
    print(u)