p=float(input("Enter the initial principal balance ammount :"))
r=float(input("Enter the intrest rate:"))
n=int(input("Enter the number of times interest applied per time period:"))
t=float(input("Enter the number of time periods elapsed:"))
ci=p*(pow((1 + r / 100), n*t))
print("The future value is:",ci)

'''  -----------------output---------------------
Enter the initial principal balance ammount :1000
Enter the intrest rate:2
Enter the number of times interest applied per time period:1
Enter the number of time periods elapsed:2
The future value is: 1040.4
-------------------------------------------'''   