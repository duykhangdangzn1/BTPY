n=int(input())
s=((1+n)*(n-1+1))/2
rc=(n/5)*5
z1=((n/5)*5)+3
r=0
z=0
if rc < n :
 r=(5+rc)*(rc-5)/5/2
else:
 c1=rc-5
 r=(5+c1)*(c1-5)/5/2
if z1 < n :
 z=(8+z1)*(z1-8)/5/2
else:
 c=z1-5
 z=(8+c)*(c-8)/5/2
print(s-r-z)
