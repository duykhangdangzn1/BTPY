l=int(input())
r=int(input())
k=int(input())
s=0
z=l//k
if z*k==l:
    z-=1
for i in range((z)+1,(r//k)+1):

    s+=(i*k)
print(s)