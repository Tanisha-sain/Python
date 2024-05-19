# print nth Fibonacci number : 0 1 1 2 3 5 8 13 21 34 ....

n = int(input("Enter a number: "))
if(n<=0):
    print("enter a non-zero positive integer")
    exit()

first = 0
second = 1
if(n == 1):
    ans = 0
elif(n == 2):
    ans = 1
else:
    for i in range(3,n+1):
        ans = first + second
        first = second
        second = ans
print(ans)