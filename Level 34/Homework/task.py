# Filter out the geese
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    return [bird for bird in birds if bird not in geese]

# Beginner Series #2 Clock
def past(h, m, s):
    return (h * 3600 + m * 60 + s) * 1000

# Name on billboard
def billboard(name, price=30):
    cost = 0
    for char in name:
        cost += price
    return cost

# What's the real floor?
def get_real_floor(n):
    if n <= 0:
        return n  
    elif n < 13:
        return n - 1 
    else:
        return n - 2 