# 
# List Filtering
def filter_list(l):
    final_list = []
    for i in l:
        if type(i) == int:
            final_list.append(i)
    return final_list
# Jaden Casing Strings
def to_jaden_case(string):
    return " ".join([i.capitalize() for i in string.split()])

# Sum of Digits / Digital Root
def digital_root(n):
    while n >= 10:
        n = sum(int(i) for i in str(n))
    return n
   