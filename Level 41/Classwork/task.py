# vowels count
def get_count(sentence):
    vowels="aeiou"
    count = 0
    for i in sentence:
        if i in vowels:
            count += 1
    return count

# Square Every Digit
def square_digits(num):
    result = ""
    for i in str(num):
        result += str(int(i) ** 2)  
    return int(result)

# Highest and Lowest
def high_and_low(numbers):  
    nums = list(map(int, numbers.split()))  
    max_num = nums[0]  
    min_num = nums[0]  
    
    for num in nums:
        if num > max_num:
            max_num = num  
        if num < min_num:
            min_num = num  
    
    return f"{max_num} {min_num}"  

# Get the Middle Character
def get_middle(s):
    length = len(s)
    if length % 2 == 0:  # Even length
        return s[length // 2 - 1 : length // 2 + 1]
    else:  # Odd length
        return s[length // 2]
  
