# a decorator that measures the time a function takes to execute

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(2)



# a decorator to print the function name and the values of its arguments every time the function is called.

def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k,v in kwargs.items())
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

@debug
def hello():
    print("hello")

@debug
def greet(name, greeting = "Hello!"):
    print(f"{greeting}, {name}")

greet("chai", greeting="hanji")
hello()


# a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the funciton.

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            print(f"returning from cache {cache_value}")
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        print(f"executing the function {cache_value}")
        return result
    return wrapper

@cache
def long_running_function(a,b):
    print(f"Taking 4 seconds to execute")
    time.sleep(4)
    return a+b

print(long_running_function(2,3))
print(long_running_function(4,7))
print(long_running_function(1,2))
print(long_running_function(2,3))
print(long_running_function(6,5))

