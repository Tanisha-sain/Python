# Calculate the factorial of a given number

n = int(input("Enter a number: "))

if(n < 0):
    print("Enter a non-negative integer")
    exit()
fact = 1

while(n > 0):
    fact = fact*n
    n = n-1
print(fact)