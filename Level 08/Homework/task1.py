"""ვუბეჭდავთ მომხმარებელს თავის სახელს გვარს მისამართს ტელეფონის ნომერს და ემაილს"""

#ვქმნით ცვლადს input სახელის შეყვანით
name = input("Enter your name: ")
#ვქმნით ცვლადს input გვარის შეყვანით
surname= input("Enter your surname: ")
#ვქმნით ცვლადს input  მისამართის შეყვანით
address = input ("Enter your address: ")
##ვქმნით ცვლადს input ტელეფონის ნომრის შეყვანით
phone_number = input("Enter your phone number: ")
#ვქმნით ცვლადს input ელფოსტის შეყვანით
Email = input("Enter your Email: ")
#ვაერთიანებთ ორ ცვლადს რომ მივიღოთ სრული სახელი და გვარი
full_name= (name + surname)
#ვბეჭდავთ ყველა მოქმედებას 
print("Hello" + full_name , "your adress is" + address, "your phone number is" + phone_number, "your email is" + Email)