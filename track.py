print("Begin")

print("Track your Monthly Expenses!")
try:
    a=input("Enter your name:")
    b=int(input("Enter your Monthly Income(Rs.):"))
    x={}
    while True:       
        i=int(input("Enter '1' to ADD NEW BILL (or) Enter '0' to CALCULATE TOTAL:"))
        if i==1:
            try:
                 i=input("Enter new bill:")
                 j=int(input("Enter amount:"))
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
    print("New Bill: \n",p[0],"\n Amount: \n",p[1])
    sum=sum+p[1]
print("Hello ",a,"!\nYour Monthly Income(Rs.):",b)
print("Total Amount Spent:",sum)
y=b-sum
print("savings:",y)

print("End")

