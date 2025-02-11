// 1) შექმენით 4 ცვლადი თითოეულ მათგანს მნიშვნელობად მიანიჭეთ განსხავებული რიცხვები შემდეგ კი ამ რიცხვებით რომლებსაც ინახავთ ცვლადებში ყველა შესაძლო კომბინაციით შეასრულეთ ოთხი მათემატიკური მოქმედება: მიმატება, გამოკლება, გამრავლება, გაყოფა ისე რომ დაიბეჭდოს თვითონ მოქმედება და პასუხი მაგ. ავიღოთ ორი რიცხვი 3 და 4 ამ ორი რიცხვის შემთხვევაში შედექი იქნება 3 + 4 = 7
// 3 - 4 = -1 და ასე შემდეგ ყველა შესაძლო რიცხვების კომბინაციით და მოქმედებით

// 2) მომხმარებელს შემოატანინეთ 2 რიცხვი, ხოლო შემდეგ გაკეთეთ ამ რიცხვებზე ყველა მათემატიკური ოპერაცია ცალცალკე

// 3) მომხმარებელს შემოატანინეთ თავისი სახელი და გავარი, შემდეგ კი ტერმინალში გამოიტანეთ მომხმარებლის შემოტანილი მნიშვნელობები

//  4) შექმენი ორი input შეადარე ორი რიცხვი და დაბეჭდე შედეგი.
//     5) შექმენი 2 ცვლადი შეამოწმე, ტოლია თუ არა ორი რიცხვი. 
//     6) მომხმარებელს შემოახანინე input შეამოწმე, არის თუ არა რიცხვი 50-ზე ნაკლები.
//     7)შემოიტანე 2 input შეამოწმე, არის თუ არა ორი რიცხვის ჯამი 100-ზე მეტი.
//     8) მომხარებელს შემოატანინე input შეამოწმე, არის თუ არა რიცხვი 10-ზე მეტი ან ტოლი.
//     9)შემოიტანე 1 input და 1 ცლადი შეადარე, არის თუ არა ერთი რიცხვი მეორეზე ნაკლები ან ტოლი.
//     10) მომხმარებელს შემოატანინეთ სახელი და შეამოწმეთ ეს სახელი უდრის თუ არა თქვენს სახელს
//    11) მომხმარებელს შემოატანინეთ პაროლი შემდეგ კითხეთ ხელახლა რომ გაიმეოროს პაროლი და შეამოწმეთ უდრის თუ არა ისინი ერთმანეთს 




// დავალება 1

// ცვლადები

var num1 = 5
var num2 = 10
var num3 = 1
var num4 = 20


// მიმატება გამოკლება
console.log("5 + 10 = " + num1 + num2)
console.log("5 - 10 = " + num1 - num2)
console.log("10 - 5= " + num2 - num1)
console.log("10 + 5 = " + num2 + num1)
console.log("10 + 1 = " + num2 + num3)
console.log("10 - 1 = " + num2 - num3)
console.log("1 + 10 = " + num3 + num2)
console.log("1 - 10 = " + num3 - num2)
console.log("1 + 20 = " + num3 + num4)
console.log("1 - 20 = " + num3 - num4)
console.log("20 - 1 = " + num4 - num3)
console.log("20 + 1 = " + num4 + num3)
console.log("5 + 1 = " + num1 + num3)
console.log("5 - 1 = " + num1 - num3)
console.log("1 + 5= " + num3 + num1)
console.log("1 - 5= " + num3 - num1)
console.log("5 + 20 = " + num1 + num4)
console.log("5 - 20 = " + num1 - num4)
console.log("20 - 5 = " + num4 - num1)
console.log("20 + 5 = " + num4 + num1)
console.log("10 + 20 = " + num2 + num4)
console.log("10 - 20 = " + num2 - num4)
console.log("20 - 10 = " + num4 - num2)
console.log("20 + 10 = " + num4 + num2)

// გამრავლება გაყოფა

console.log("5 * 10 = " + num1 * num2)
console.log("5 // 10 = " + num1 / num2)
console.log("10 // 5= " + num2 / num1)
console.log("10 * 5 = " + num2 * num1)
console.log("10 * 1 = " + num2 * num3)
console.log("10 // 1 = " + num2 / num3)
console.log("1 * 10 = " + num3 * num2)
console.log("1 // 10 = " + num3 / num2)
console.log("1 * 20 = " + num3 * num4)
console.log("1 // 20 = " + num3 / num4)
console.log("20 // 1 = " + num4 / num3)
console.log("20 * 1 = " + num4 * num3)
console.log("5 * 1 = " + num1 * num3)
console.log("5 // 1 = " + num1 / num3)
console.log("1 * 5= " + num3 * num1)
console.log("1 // 5= " + num3 / num1)
console.log("5 * 20 = " + num1 * num4)
console.log("5 // 20 = " + num1 / num4)
console.log("20 // 5 = " + num4 / num1)
console.log("20 * 5 = " + num4 * num1)
console.log("10 * 20 = " + num2 * num4)
console.log("10 // 20 = " + num2 / num4)
console.log("20 // 10 = " + num4 / num2)
console.log("20 * 10 = " + num4 * num2)


// დავალება 2

var usernum1 = prompt("Num: ")

var usernum2 = prompt("Num: ")

console.log(usernum1 + usernum2)
console.log(usernum1 - usernum2)
console.log(usernum1 * usernum2)
console.log(usernum1 / usernum2)


// დავალება 3

var name = prompt("Name: ")
var surname =  prompt("Surname: ")

console.log( name + " " + surname)

// დავალება 4

var number = prompt("Num: ")

var number1 = prompt("Num: ")

console.log(number > number1)
console.log(number < number1)
console.log(number = number1)

// დავალება 5

var number2 = 10
var number3 = 15

console.log(number2 == number3)

//დავალება 6

var usernum1 = prompt("Num: ")

console.log(usernum1 > 50)


// დავალება 7

var num10 = prompt("Num: ")
var num01 = prompt("Num: ")

console.log(num10 + num01 > 100)

// დავალება 8

var num999 = prompt("Num: ")

console.log(num999 >= 10)

// დავალება 9

var num099 = prompt("Num: ")
var num00 = 100

console.log(num00 <= num099)

// დავალება 10

var username_1 = prompt("Name: ")

console.log(username_1 = "Giorgi")

// დავალება 11

var userpass = prompt("Password: ")
var userpass_again = prompt("Enter it again: ")

console.log(userpass = userpass_again)

