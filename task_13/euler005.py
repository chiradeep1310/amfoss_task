t=int(input())
for i in range (t):
    n=int(input())
    list=[]
    list1=[]
    for k in range(1,n+1):
        c=0
        for j in range(2,k+1):
            if k%j==0:
                c+=1
        if c==1:
            list.append(k)
    for k in range(len(list)):
        for j in range (n):
            if (list[k]**j)<=n and (list[k]**(j+1))>n:
                list1.append(list[k]**j)
    s=1
    for k in range (len(list1)):
       s=list1[k]*s
    print(s)
    
       
        
    
        
            
