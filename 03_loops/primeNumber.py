# Check if a number is prime or not
import math

num = int(input("enter a number: "))
prime = True

if(num < 2):
    prime = False

if(num > 2):
    for i in range(2,int(math.sqrt(num)) + 1):
        if(num%i == 0):
            prime = False
            break
if(prime):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")