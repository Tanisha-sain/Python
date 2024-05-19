import math

# function with one parameter
def square_of_num(num):
    return num**2

# function with two parameters
def add(num1, num2):
    return num1+num2

# function which works with more than one data type
def multiply(inp1, inp2):
    return inp1*inp2

# function which is returning multiple values
def area_circum(radius):
    area = math.pi * radius * radius
    circum = 2 * math.pi * radius
    return area, circum

# function with a default parameter
def greet(name = "User"):
    print("Hello", name,"!")

# function which takes variable arguments
def sum_all(*args):
    return sum(args)

# function which takes variable keyword argument
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Generator function with yield
def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i

# Recursive function
def factorial(num):
    if(num < 0):
        return
    if(num == 0 or num == 1):
        return 1
    return num*factorial(num-1)

# Lambda Funcion ------
cube = lambda x : x**3


print(factorial(5))
for num in even_generator(10):
    print(num)

print_kwargs(name = "Tanisha", age = 19, branch = "AIML")
print_kwargs(name = "Shaktimaan", power = "lazer")
print(sum_all(1,2,3,4,5))
print(cube(3))


sq = square_of_num(5)
sum = add(5,6)
# print(sq)
# print(sum)
# print(multiply(5,10))
# print(multiply("Tanisha ", 3))
# print(multiply("Hello",5))

(area, circum) = area_circum(7)
print("Area of circle is", round(area,2), "and circumference of circle is", round(circum,2))

greet()
greet("Tanisha")

