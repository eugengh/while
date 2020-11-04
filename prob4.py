b=1
s=0
p=1 
n=eval(input("n="))
while b<=n:
    s+=b
    p*=b
    b+=1

print("suma este " +str(s))
print("produsul este " +str(p))
print("Media aritmetica este " + str(round(s/n,)))
