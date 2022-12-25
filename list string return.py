a=list(map(str,input().split()))
b=input()
l1=[]
l2=[]
for p in b:
    l1.append(p)
#print(l1)
for i in a:
    for j in i:
        #l2.append(j)
        #print(l2)
        if p in j:
            l2.append(i)
print(l2)



        
        
