print("Begin")

print("Split Bills with your Friends for a Trip/Hangout/Dinner outside!")
try:
    x={}
    while True:       
        i=int(input("Enter '1' to ADD Friend (or) Enter '0' to CALCULATE TOTAL:"))
        if i==1:
            try:
                 i=input("Enter Friend Name:")
                 j=int(input("Enter Bill Amount(Rs.):"))
            except(ValueError):
                print("Please! \n Fill given fields!")
                break
            x[i]=j
        else:
            break
        
except(ValueError):
         print("Please! \n Enter numericals ONLY!")
       
print(x)
kv=x.items()
sum=0
for p in kv:
    print("Friend Name:",p[0],"\nBill Amount:",p[1])
    sum=sum+p[1]

print("Total Amount:",sum)


print("End")
