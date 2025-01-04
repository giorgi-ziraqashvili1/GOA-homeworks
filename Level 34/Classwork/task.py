# Grasshopper - Summation
def summation(num):
    return num * (num + 1) // 2
# Remove String Space
def no_space(x):
    result = ""
    for i in x:
        if i != " ":
            result += i
    return result
# Keep Hydrated!
def litres(time):
    return int(time * 0.5) 
# Century From Year
def century(year):
    return (year + 99) // 100
# Convert number to reversed array of digits
def digitize(n):
    return [int(i) for i in str(n)][::-1]