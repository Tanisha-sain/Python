# Print the multiplication table for a given number upto 10 but skip the fifth iteration

n = int(input("Enter a number: "))

for i in range(1,11):
    if (i == 5):
        continue
    print(n , "X" , i , "=" , (n*i))