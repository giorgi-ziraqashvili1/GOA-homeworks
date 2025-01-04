
# Beginner Series #1 School Paperwork
def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    return n * m

# Abbreviate a Two Word Name
def abbrev_name(name):
    names = name.split() 
    return f"{names[0][0].upper()}.{names[1][0].upper()}"

# Are You Playing Banjo?\
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    
# Simple multiplication
def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
    

# A Needle in the Haystack
def find_needle(haystack):
     for i in range(len(haystack)):
        if haystack[i] == "needle":
            return "found the needle at position " + str(i)