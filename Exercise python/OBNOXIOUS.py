q = int(input()) 
st = []

for i in range(100002):
     if i % 3 != 0 and i % 10 != 3 :
            st.append(i)  

for j in range(q):
    k=int(input())
    c=k-1
    print(st[c])
