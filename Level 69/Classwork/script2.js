//2) მომხმარებელს შემოატანინეთ რიცხვი, შემდეგ შემოატანინეთ არჩევანი(ერთიდან მომხმარებლის რიცხვამდე დაბეჭდოს ლუწი, კენტი, კვადრატი ან 3 ის ჯერადი რიცხვი

var userNum = prompt("Enter num: ")
var num = 1

var user_archevan = prompt("enter your archevan")

while(num > userNum){
    num += 1

    if(num % 2 == 0  && user_archevan == "ლუწი"){
        console.log(num)
    }if(num % 2 != 0 && user_archevan == "კენტი"){
        console.log(num)
    }if(num % 3 == 0 && user_archevan == "სამის ჯერადი"){
        console.log(num)
    }if(user_archevan == "კვადრატი")
        console.log(num * num)
    }


    