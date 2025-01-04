
# Counting sheep...
def count_sheeps(sheep):
    return sheep.count(True)

# Check the exam
def check_exam(arr1,arr2):
    score = 0
    for k, a in zip(arr1, arr2):
        if a == k:
            score += 4
        elif a == '':
            score += 0
        else:
            score -= 1
    return max(score, 0)

# Find Multiples of a Number
def find_multiples(integer, limit):
    arr = []
    count = integer
    while count <= limit:
        arr.append(count)
        count += integer
    return arr

# Sum Mixed Array

def sum_mix(arr):
     return sum(int(x) for x in arr)

# Fake Binary
def fake_bin(x):
    return ''.join('0' if int(digit) < 5 else '1' for digit in x)
