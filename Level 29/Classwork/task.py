
# 1)შექმენით ფუნქცია რომელსაც გადაეცემა სია,გამოითვალეთ რიცხვების ჯამი for ციკლის საშუალებითაც და sum() ფუნქციის გამოყენებითაც აუცილებლად დააბრუნეთ შედეგი return ის გამოყენებით.

def list_sum(num):
    return sum(num)

print(list_sum([1,2,3,4,5]))


# for ციკლით

def list_sum1(num2):
    sum = 0
    for i in num2:
        sum += i
    return sum
    
print(list_sum1([1,2,3,4,5,6]))







