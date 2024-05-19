# Calculate the sum of even numbers up to a given number n

n = int(input("Enter a number n: "))

sum = 0
for i in range(2,n+1,2):
    print(i)
    sum += i
print(sum)