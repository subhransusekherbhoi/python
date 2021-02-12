n=int(input("Enter the number to calculate it's factorial"))
f=1
if n==0:
    print("The factorial is:1") 
elif n<0:
    print("Factorial of negative number doesn't exsist")    
else:
    for i in range(1,n+1):
        f=f*i
    print("factorial is:",f) 

'''  -----------------output---------------------
Enter the number to calculate it's factorial5
factorial is: 120
-------------------------------------------'''   
   