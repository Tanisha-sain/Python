# reverse a string using a loop

string = input("Enter a string: ")
rev_str = ""

for char in string:
    rev_str = char + rev_str
print(rev_str)