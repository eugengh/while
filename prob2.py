l=1
sp=0
sn=0
np=0
nn=0
while l<=12:
    temp=eval(input("Introduceti temperaturile: "))
    if temp>0:
        sp+=temp
        np+=1
    if temp<0:
        sn+=temp
        nn+=1
    l+=1
 

print("Media t. pozitive este"+str( round(sp/np, 2)))
print("Media t. negative este"+str( round(sn/nn, 2 )))