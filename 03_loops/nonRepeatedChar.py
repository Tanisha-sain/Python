# Given a string, find the first non repeated character

input_str = "teeter"

for char in input_str:
    if(input_str.count(char) == 1):
        print(char)
        break