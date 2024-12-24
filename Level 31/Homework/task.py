# # Write a function `greet` that returns "hello world!"

def greet():
    return "hello world!"

# Opposite number
def opposite(number):
    return number - number * 2

# Return Negative
def make_negative( number ):
    if number > 0 :
        return number - number * 2
    elif number == 0 :
        return number
    else:
        return number
    

# Sum of positive
def positive_sum(arr):
        sum = 0
        if arr > 0:
            for i in arr:
                sum += i
            return sum
        else:
            return 0

# String repeat
def repeat_str(repeat, string):
    return repeat * string

# Square(n) Sum
def square_sum(numbers):
    sum = 0
    for i in numbers:
        sum += i *  i
    return sum
# Find the smallest integer in the array
def find_smallest_int(arr):
    return min(arr)

# Grasshopper - Summation
def summation(num):
    sum = 0
    while sum < num:
        sum += 1
    return sum

# space remover
def no_space(x):
     return x.replace(" ", "")

# Counting sheep...
def count_sheeps(sheep):
    return sheep.count(True)