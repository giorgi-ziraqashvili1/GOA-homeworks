# 1)კომენტარებით ახსენით განსხვევება indexing-სა და sliceing-ს შორის.
 
# indexing სა და sliceing შორის განსხვავება ის არის რომ sliceing ის სიიდან შეუძ₾ია ამოჭრას ნებისმიერი ელემენტი

# 2)შექმენით სია სადაც გექნებათ 5 ელემენტი და მინუს ინდექსების გამოყენებით გამოიტანეთ ბოლო 3 ელემენტი

list = ["hey","Hello","Gamarjoba","Ola","haii"]

print(list[-3:])

# 3)შექმენით სია სადაც გექნებათ 10 რიცხვი, გადაუარეთ ამ სიას და გამოიტანეთ მხოლოდ ის რიცხვები რომელიც მეტია ან ტოლია 10ზე

nums= [10,20,30,40,50,5,3,2,1,8]
for i in nums:
    if i >= 10:
        print(i)


# 4)კომენტარის სახით ახსენით რა არის ფუქნცია, რაში ვიყენებთ და ჩამოწერეთ ყველა ნასწავლი ფუნქცია (გვერდით მიუწერეთ მათი დანიშნულება)
# ფუნქცია არის ყველა ის კოდი რომელსაც აქვს ფრჩხილები და ამ ფუნქციას შეუძლია რაიმე დავალების შესრულება

# print() გამოტანა 
# input() მომხარებლის მიერ ტექსტის შეყვანა
# range() დიაპაზონი
# type() კოდის ტიპის გაგება
# str() ტექსტის ტიპით ჩაწერა
# float() ატწილადი
# int()მთელი რიცხვი

# 5)(***BOSS LEVEL***) მომხმარებელს შემოატანინეთ მისი გვარი, შემდეგ შეეკითხეთ უნდა თუ არა რომ მისი გვარი გადაიყვანოს დიდ ასოებად, თუ გიპასუხათ "yes" მაშინ დაუბეჭდეთ მისი სახელი დიდი ასოებით, თუ გიპასუხათ "no" დაუბეჭდეთ უბრალოდ მისი სახელი. (მინიშნება: გაკვეთილის ბოლოს განვიხილეთ ზედაპირულად)


surname= input("Enter yur surname: ")

answer= input("you want to make your surname in upper case?(yes or no): ")

yes = "yes"

no= "no"

if answer == yes:
    print(surname.upper())

elif answer == no :
    print(surname)


