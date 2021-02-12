n=int(input("Enter a number"))
sum=0
temp=n
while temp > 0:
    r=temp % 10
    sum+=pow(r,3)
    temp//=10
if n==sum:
    print("The number is an armstrong number")
else:
    print("The number is not an armstrong number")      
'''  -----------------output---------------------
Enter a number407
The number is an armstrong number
-------------------------------------------'''   