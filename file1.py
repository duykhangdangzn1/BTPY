fi=open('input.txt','r')
fo=open('output.txt','w')
c=fi.readline().split()
s=[]
for i in c :
    s.append(int(i))
a=s[0]
b=s[1]
k=s[2]
if (a + b) % k == 0 :
    c=a+b 
    fo.write(str(c))
else:
    c=0
    fo.write(str(c))
