print("Begin")
t=input("What kind of Trip are you planning ?")
x={}
while True:
    a=int(input("Enter '1' to ADD NEW FRIEND (or) '0' to CALCULATE TOTAL AMOUNT:"))
    if a==1:
        i=input("Enter New Name:")
        j=int(input("Enter their Amount:"))
        x[i]=j
    else:
        break
print(x)
kv=x.items()
sum=0
for p in kv:
    print(p[0],p[1])
    sum=sum+p[1]
print("Total",sum)
    
    
print("End")
