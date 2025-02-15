n = int(input("Enter the Number of Terms : "))
t1=0
t2=1
nexT=t1+t2
print("Fibonacci Series:", t1, t2, end=" ")

for i in range(2,n):
    print(nexT, end=" ") 
    t1=t2
    t2=nexT
    nexT=t1+t2