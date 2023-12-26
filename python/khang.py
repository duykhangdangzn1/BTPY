fi=open("INPUT.TXT",'r')
fo=open("OUTPUT.TXT",'w')
n,s=map(int,fi.read().split())
passw= "9" * n
c=int(passw)
s1=0
max_sum = 9 * n
if s > max_sum:  
    fo.write("-1")
else:
    c = 10**n - 1
    while c > 0:
        s1 = sum(int(d) for d in str(c)) 
        if s1 == s:
            fo.write(str(c) + '\n') 
            break
        c -= 1