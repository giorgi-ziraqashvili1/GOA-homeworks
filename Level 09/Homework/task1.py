"""1)მომხმარებელს შემოატანინეთ მისი ასაკი და გაიგეთ რამდენჯერ მოთავსდება რიცხვი 10 მასში"""

age = int(input("Enter your age: "))

print(age // 10)

"""2)მომხმარებელს შემოატანინეთ მისი სახელი და გაიგეთ უდრის თუ არა ის თქვენს სახელს"""

name = input("enter your name: ")

my_name = "Giorgi"

print(name == my_name)

"""3)მომხმარებელს შემოატანინეთ ორი რიცხვი (num1 და num2) და გაიგეთ რა იქნება ნაშთი, პირველი რიცხვის მეორეზე გაყოფის შემდეგ"""


num1= int(input("enter your num1: "))
num2= int(input("enter your num2: "))

print(num1 % num2)

"""4)მომხმარებელს შემოატანინეთ მისი ასაკი და გაიგეთ არის თუ არა ის ლუწი (იყოფა თუ არა ზუსტად 2ზე) ანუ გვრჩება თუ არა ნაშთი ნული, ორზე გაყოფის შედეგად"""

age2 = int(input("enter your age: "))

print(age2 % 2)
