# Given a list of numbers, count how many are positive

numbers = [1,-3,2,5,-67,7,9,10,-1,56,9,-12]
count = 0
for num in numbers:
    if(num > 0):
        count += 1

print(count)
