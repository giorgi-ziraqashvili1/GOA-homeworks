# .lower() ტექსტის პატარა ასოებით დაწერა
# .upper() ტექსტის დიდი ასოებით დაწერა
# .capitalize() წერს მხოლოდ პირველ ასოს დიდად
# .find() ეძებს ასოს თუ რამდენჯერაა გამოყენებული სიტყვაში
  

# 2)მომხმარებელს შემოატანინეთ მისი გვარი და შეამოწმეთ, თუ გვარის პირველი ასო არის დიდი ასო, მაშინ დაუბეჭდეთ "Hello", თუ არ არის მაშინ დაუბეჭდეთ "Bye"

user= input("Enter your surname: ")

if user.capitalize() == user:
    print("Hello")
else:
    print("bye")

# 3)მომხმარებელს შემოატანინეთ სახელი, შემდეგ შემოატანინეთ ასო და თუ ამ სახელში ეს ასო არიქნება, მაშინ გამოუტანეთ "Can't find character", თუ იქნება მაშინ გამოუტანეთ "found it" და გვერდზე მიუწერეთ ამ ასოს ინდექსი

user1= input("enter your name: ")
letter=input ("enter your letter: ")

if user1.find(letter):
    print("found it")
else:
    print("Can't find character")

# 4)მომხმარებელს შემოატანინეთ მისი გვარი, შემდეგ შეეკითხეთ როგორ უნდა რო შეიცვალოს მისი გვარის ასოები, თუ გიპასუხებთ "upper" გადაიყვანეთ მთლიანი გვარი დიდ ასოებად, თუ გიპასუხებთ "lower" გადაიყვანეთ მთლიანი გვარი პატარა ასოებად და თუ გიპასუხებთ "capitalize" გადაიყვანეთ გვარის მხოლოდ პირველი ასო დიდ ასოდ.
surname= input("Enter yur surname: ")

answer= input("you want to make your surname in (upper,lower or capitalize) : ")

upper = "upper"

lower= "lower"

capitalize= "capitalize"

if answer == upper:
    print(surname.upper())

elif answer == lower :
    print(surname)

elif answer == capitalize:
    print(surname.capitalize())