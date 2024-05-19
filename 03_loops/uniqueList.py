# Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate

list = ["apple", "orange", "banana", "apple", "pineapple", "orange"]

unique_item = set()

for fruit in list:
    if fruit in unique_item:
        print("Duplicate :", fruit)
        break;
    unique_item.add(fruit)
    